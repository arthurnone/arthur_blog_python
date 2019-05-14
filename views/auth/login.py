#!/usr/bin/env python
# coding:utf-8
from flask import request
from views.base import BaseHandler
from models.user import User
from models.session import Session
from utils import check_code


class LoginHandler(BaseHandler):

    def post(self):
        formdata = request.get_json()
        code = formdata["code"]
        if !check_code(code):
            res = self.json_response(status=0, data={}, msg="fail.")
            return res

        userdb = User()
        login = userdb.login(username=formdata["username"], password=formdata["password"])
        if login["status"]:
            session_id = login["session_id"]
            res = self.json_response(status=1, data={}, msg="success")
            res.set_cookie(key='session_id', value=session_id, max_age=86400)
        else:
            res = self.json_response(status=0, data={}, msg="fail")
        return res


class LoginOutHandler(BaseHandler):

    def get(self):
        session_id = request.cookies.get("session_id")
        Session().delete(session_id)

        res = self.json_response(status=1, data={}, msg="success")

        if session_id:
            res.set_cookie(key='session_id', value=session_id, max_age=0)

        return res
