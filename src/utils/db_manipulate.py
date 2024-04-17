from typing import Dict, List
from datetime import datetime, timedelta
import json

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection
)


class _DBManipulator:
    """
    An internal class to simplify the bot's interaction with the database.
    """

    def __init__(self, *, host: str, port: int, db_name: str, col_name: str) -> None:
        # Connecting to database
        self.__client: AsyncIOMotorClient = AsyncIOMotorClient(host, port)
        self.__db: AsyncIOMotorDatabase = self.__client[db_name]
        self.__collection: AsyncIOMotorCollection = self.__db[col_name]

    async def get_data(self, *, data: Dict[str, str]) -> str | None:
        data_for_send: Dict[str, List[int | str]] = {'dataset': [], 'labels': []}
        dt_from: datetime = datetime.fromisoformat(data.get('dt_from', ''))
        dt_upto: datetime = datetime.fromisoformat(data.get('dt_upto', ''))
        group_type: str = data.get('group_type', '')

        # Create a dictionary with grouping
        dt_dict: Dict[str, int] = dict()
        dt_diff: timedelta = dt_upto - dt_from
        hour_diff: int = (dt_diff.days * 24) + (dt_diff.seconds // 3600)
        for hours in range(hour_diff + 1):
            temp_dttm: datetime = dt_from + timedelta(hours=hours)
            new_dttm: str = datetime(
                year=temp_dttm.year,
                month=temp_dttm.month,
                day=temp_dttm.day if group_type in ('day', 'hour') else 1,
                hour=temp_dttm.hour if group_type == 'hour' else 0
            ).isoformat()
            if not dt_dict.get(new_dttm):
                dt_dict[new_dttm] = 0

        # Get the query results
        cursor = self.__collection.find(
            {
                '$and': [
                    {'dt': {'$gte': dt_from}},
                    {'dt': {'$lte': dt_upto}}
                ]
            }
        ).sort('dt')

        # Editing the query results
        async for doc in cursor:
            doc_dttm = datetime(
                year=doc.get('dt').year,
                month=doc.get('dt').month,
                day=doc.get('dt').day if group_type in ('day', 'hour') else 1,
                hour=doc.get('dt').hour if group_type == 'hour' else 0
            ).isoformat()
            dt_dict[doc_dttm] += doc.get('value', 0)
        
        for dttm, summ in dt_dict.items():
            data_for_send['dataset'].append(summ)
            data_for_send['labels'].append(dttm)
        

        return json.dumps(obj=data_for_send)
