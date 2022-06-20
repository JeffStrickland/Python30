"""
Day 20 - Context Managers

Try to solve one of your problems by creating a context
manager, I give you some suggestions:
- Open and close the browser (Selenium).
- Connect and Close the connection of a database.
"""
from pymongo import MongoClient

class Connect_Manager_Mongo():
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.hostnmae, self.port)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conncetion.close()

with Connect_Manager_Mongo('localhost', '27017') as mongo:
    collection = mongo.conncetion.SampleDb.test
    data = collection.find({'__id': 1})
    print(data.get('name'))


"""
You can investigate the "contextlib" module and see other
types of context managers you can create, try one to
*suppress* any ValueError exceptions.
"""

from contextlib import suppress

def suppress_value_error():
    return int(input("Insert a number (or not):"))

with suppress(ValueError):
    number = suppress_value_error()
    print(number, "is a number")