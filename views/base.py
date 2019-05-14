#!/usr/bin/env python
# coding:utf-8
import json
from flask.views import MethodView
from flask import make_response, request
from config import DEBUG


class BaseHandler(MethodView):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__()

    def json_response(self, status, msg='', data={}, **kwargs):
        data = {
            'status': status,
            'msg': msg,
            'data': data
        }
        data.update(kwargs)
        data = json.dumps(data)
        resp = make_response(data)
        resp.headers['Content-Type'] = 'application/json'
        resp = set_headers(resp)
        return resp

    def options(self, *args, **kwargs):
        resp = make_response()
        resp = set_headers(resp)
        return resp


def set_headers(response):
    if DEBUG:
        response.headers['Access-Control-Allow-Origin'] = request.headers.get(
            'Origin')
        response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        response.headers['Access-Control-Allow-Credentials'] = "true"
    response.headers['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept'
    response.headers['Server'] = 'Python Server'
    response.headers['Access-Control-Max-Age'] = 1678000
    return response
