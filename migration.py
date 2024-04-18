from typing import List, Dict, Any
from os import getenv

import bson
from pymongo import MongoClient


DB_HOST: str = getenv('DB_HOST') # type: ignore
DB_PORT: int = int(getenv('DB_PORT')) # type: ignore
CLIENT: MongoClient = MongoClient(
    host=DB_HOST,
    port=DB_PORT
)


def migrate() -> None:
    if not 'test_collection' in CLIENT.test_db.list_collection_names():
        with open(file='dump/sample_collection.bson', mode='rb') as bson_data:
            decode_data: List[Dict[str, Any]] = bson.decode_all(data=bson_data.read())
        CLIENT.test_db.test_collection.insert_many(documents=decode_data)


if __name__ == '__main__':
    migrate()
