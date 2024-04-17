from typing import Dict, List
import json
from json.decoder import JSONDecodeError
from re import match

from loguru import logger
from aiogram.types import Message
from aiogram.filters import BaseFilter


class IsCorrectData(BaseFilter):
    """
    Filter class for checking and retrieving changed data.
    """

    async def __call__(self, message: Message) -> Dict[str, Dict[str, str]] | None:
        dttm_pattern: str = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$'
        list_group_pattern: List[str] = [
            'hour',
            'day',
            'month'
        ]

        try:
            py_data = json.loads(s=message.text) # type: ignore
            
            if isinstance(py_data, Dict) \
            and match(dttm_pattern, py_data.get('dt_from', '')) \
            and match(dttm_pattern, py_data.get('dt_upto', '')) \
            and py_data.get('group_type') in list_group_pattern \
            and len(py_data) == 3:
                return {'cor_data': py_data}
            else:
                raise TypeError
            
        except (JSONDecodeError, TypeError) as exc:
            logger.exception(exc)
