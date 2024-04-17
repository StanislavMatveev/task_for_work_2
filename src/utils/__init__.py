from .db_manipulate import _DBManipulator


# Creating an instance of a class to work with a MongoDB
mongodb_manipulator: _DBManipulator = _DBManipulator(
    host='localhost',
    port=8081,
    db_name='test_db',
    col_name='test_collection',
)
