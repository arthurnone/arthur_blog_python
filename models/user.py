#!/usr/bin/env python
# coding:utf-8
from .base import BaseMongoDB
from utils import str2md5, generate_rand_id
from .session import Session
import datetime


class User(BaseMongoDB):
    collection_name = "user"

    def hash(self, password, salt):
        hashpwd = str2md5(password)
        return str2md5("{}-{}".format(hashpwd, salt))

    def create(self, username, password, nickname):
        salt = generate_rand_id()
        hashpwd = self.hash(password, salt)
        user = {
            "_id": username,
            "pwd": hashpwd,
            "nickname": nickname,
            "salt": salt,
            "create_time": datetime.datetime.now()
        }
        self.save(user)
        user["status"] = True
        return user

    def check_pwd(self, form_pwd, user_pwd, user_salt):
        hash = str2md5("{}-{}".format(form_pwd, user_salt))
        if hash == user_pwd:
            return True
        else:
            return False

    def get(self, uid):
        user = self.db[self.collection_name].find_one({"_id": uid})
        return user

    def login(self, username, password):
        data = {
            "status": False,
            "session_id": ""
        }
        user = self.get(username)
        if user:
            check_pwd = self.check_pwd(password, user["pwd"], user["salt"])
            if check_pwd:
                session_id = Session.set(user["_id"])
                data["session_id"] = session_id
                data["status"] = True

        return data
