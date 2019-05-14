#!/usr/bin/env python
# coding:utf-8
from flask import request
from views.base import BaseHandler
from models.user import User
from models.session import Session


class AuthHandler(BaseHandler):

    def get(self):
        session_id = request.cookies.get("session_id")

        if session_id:
            session = Session.get(session_id)
            uid = session.user_id.decode("utf-8")
            if uid:
                user = User().get(uid)
                if user:
                    data = {
                        "user": uid,
                        "nickname": user["nickname"]
                    }
                    res = self.json_response(status=1, data=data, msg="")
                    return res

            res = self.json_response(status=0, data={}, msg="")
            return res
        else:
            res = self.json_response(status=0, data={}, msg="")
            return res
