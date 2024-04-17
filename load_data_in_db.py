from typing import List, Dict, Any

import bson
from pymongo import MongoClient


CLIENT: MongoClient = MongoClient(
    host='localhost',
    port=8081
)


def load_db() -> None:
    with open(file='dump/sample_collection.bson', mode='rb') as bson_data:
        decode_data: List[Dict[str, Any]] = bson.decode_all(data=bson_data.read())
    
    CLIENT.test_db.test_collection.insert_many(documents=decode_data)


if __name__ == '__main__':
    load_db()
