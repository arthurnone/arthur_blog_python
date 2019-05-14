#!/usr/bin/env python
# coding:utf-8
from __future__ import print_function
from app import app
from config import DEBUG, HOST, PORT, SCREAT_KEY

app.secret_key = SCREAT_KEY

print("host:{}, port: {}, debug: {}".format(HOST, PORT, DEBUG))

app.run(
    debug=DEBUG,
    host=HOST,
    port=PORT
)
