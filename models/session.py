#!/usr/bin/env python
# coding:utf-8
import redis
from config import REDIS_HOST, REDIS_PORT
from utils import generate_rand_id

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)


class Session(object):
    redis = r

    def __init__(self, session_id=None, user_id=None):
        self.session_id = session_id
        self.user_id = user_id

    @classmethod
    def get(cls, session_id):
        user_id = cls.redis.get(session_id)
        if user_id:
            return Session(session_id, user_id)

    @classmethod
    def set(cls, user_id):
        session_id = generate_rand_id(user_id)
        cls.redis.set(session_id, user_id, ex=86400)
        return session_id

    @classmethod
    def delete(cls, session_id):
        cls.redis.delete(session_id)
        return session_id
