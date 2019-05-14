#!/usr/bin/env python
# coding:utf-8
import json
from flask import request, make_response
from models.user import User
from models.session import Session


def json_response(status, msg='', data={}, **kwargs):
    data = {
        'status': status,
        'msg': msg,
        'data': data
    }
    data.update(kwargs)
    data = json.dumps(data)
    resp = make_response(data)
    resp.headers['Content-Type'] = 'application/json'
    return resp


def loginrequire(func):
    def wrapper(*args, **kwargs):
        session_id = request.cookies.get("session_id")

        if not session_id:
            return json_response(status=-1, msg="loginrequire")

        session = Session.get(session_id)
        if not session:
            return json_response(status=-1, msg="loginrequire")

        uid = session.user_id.decode("utf-8")
        user = User().get(uid=uid)
        if not user:
            return json_response(status=-1, msg="loginrequire")

        return func(user=user, *args, **kwargs)

    return wrapper
