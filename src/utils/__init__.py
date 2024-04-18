from .db_manipulate import _DBManipulator
from ..config.config import DBConfig


# Creating an instance of a class to work with a MongoDB
mongodb_manipulator: _DBManipulator = _DBManipulator(
    host=DBConfig.DB_HOST,
    port=DBConfig.DB_PORT,
    db_name='test_db',
    col_name='test_collection',
)
