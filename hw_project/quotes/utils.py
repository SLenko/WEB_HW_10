from pymongo import MongoClient

def get_mongodb_connection():
    client = MongoClient('mongodb://localhost')

    db = client.hw_10
    return db