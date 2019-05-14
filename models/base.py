#!/usr/bin/env python
# coding:utf-8
from __future__ import print_function
from config import MONGO_HOST, MONGO_PORT, MONGO_USERNAME, MONGO_PWD, MONGO_DBNAME

import pymongo


def conndb(host=MONGO_HOST, port=MONGO_PORT):
    try:
        client = pymongo.MongoClient('{}:{}'.format(host, port), serverSelectionTimeoutMS=2)
        if MONGO_USERNAME:
            # checkout username password
            client.admin.authenticate(MONGO_USERNAME, MONGO_PWD)
        return client
    except Exception as e:
        print(e)
        return None


client = conndb()


class BaseMongoDB(object):
    client = client
    db = None
    collection = None
    db_name = MONGO_DBNAME
    collection_name = ""
    keys = []

    def __init__(self, collection_name=None):
        if collection_name:
            self.collection_name = collection_name

        try:
            self.db = self.client[self.db_name]
            self.collection = self.db[self.collection_name]
        except Exception as e:
            print(e)

    def close(self):
        try:
            self.client.close()
        except Exception as e:
            print(e)

    def insert(self, data):
        new = {}
        for key in self.keys:
            new[key] = data[key]
        self.db[self.collection_name].insert(new)

    def update(self, mid, data):
        self.db[self.collection_name].update({"_id": mid}, {'$set': data})

    def get(self, *args, **kwargs):
        try:
            data = self.db[self.collection_name].find(*args, **kwargs)
            return data
        except:
            return []

    def get_one(self, filter, *args, **kwargs):
        try:
            data = self.db[self.collection_name].find_one(filter, *args, **kwargs)
            return data
        except:
            return None

    def save(self, data):
        try:
            self.db[self.collection_name].save(data)
        except Exception as e:
            print(e)

    def drop(self):
        try:
            self.db[self.collection_name].drop()
        except Exception as e:
            print(e)
