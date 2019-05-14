#!/usr/bin/env python
# coding:utf-8
from __future__ import print_function
from config import DIST_PATH
from .base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        try:
            f = DIST_PATH + "/index.html"
            print(f)
            with open(f, "r") as f:
                text = f.read()
            return text
        except Exception as e:
            print(e)
            return "500 error", 500


class TestHandler(BaseHandler):
    def get(self):
        res = self.json_response(status=True, data={})
        return res
