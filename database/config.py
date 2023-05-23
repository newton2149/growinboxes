from pymongo import MongoClient

import datetime

def mongo_conn():
    try:
        # conn = MongoClient(host=settings.DATABASE_HOST, port=settings.DATABASE_PORT)
        conn = MongoClient(host='127.0.0.1', port=27017)
        print("MongoDb Connected", conn)
        return conn.growinboxes
    except Exception as e:
        print(e)

db = mongo_conn()
