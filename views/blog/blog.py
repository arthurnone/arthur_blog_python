#!/usr/bin/env python
# coding:utf-8
from views.base import BaseHandler
from flask import request
from auth import loginrequire
import datetime

from models.blog import Blog
from utils import generate_rand_id


class BlogHandler(BaseHandler):
    limit = 20

    def get(self, *args, **kwargs):
        q = int(request.args.get('q', 1))
        page = {}

        if q == 1:
            p = int(request.args.get('p', 1))
            page = {
                "p": p,
                "limit": self.limit,
                "count": 0
            }
            data = Blog().get(
                {'delete': {'$ne': True}},
                {'uid': 0},
                sort=[('create_time', -1)],
                skip=self.limit * (p - 1),
                limit=self.limit
            )
            page["count"] = data.count()
            data = list(data)
        else:
            bid = request.args.get('id', None)
            data = Blog().get_one({"_id": bid})
            data.pop("uid")

        res = self.json_response(status=1, data=data, page=page)
        return res

    @loginrequire
    def post(self, *args, **kwargs):
        user = kwargs['user']
        nickname = user["nickname"]
        formdata = request.get_json()

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if formdata.get("tag"):
            formdata["tag"] = formdata["tag"].split(" ")

        if (formdata["isnew"]):
            formdata["author"] = nickname
            formdata["uid"] = user["_id"]
            formdata["_id"] = generate_rand_id()
            formdata["create_time"] = now
            formdata["update_time"] = now
            Blog().insert(formdata)
            res = self.json_response(status=1, data=formdata, msg="create new blog success!")
            return res
        else:
            # check blog uid === uid
            keys = ['title', 'body', 'type', 'tag', 'language']
            updatedata = {}
            updatedata["update_time"] = now
            for key in keys:
                updatedata[key] = formdata[key]
            Blog().update(formdata["_id"], updatedata)
            res = self.json_response(status=1, data=formdata, msg="update success!")
            return res

    @loginrequire
    def delete(self, *args, **kwargs):
        formdata = request.get_json()
        Blog().update(formdata["id"], {'delete': True})
        res = self.json_response(status=1, data=formdata, msg="update success!")
        return res
