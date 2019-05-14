#!/usr/bin/env python
# coding:utf-8
from __future__ import print_function
import os

# BASE CONFIG
DEBUG = False
HOST = "0.0.0.0"
PORT = 2019

SCREAT_KEY = ""

# path
PATH = os.path.abspath(os.path.dirname(__file__))
WWW_PATH = os.path.abspath(os.path.dirname(PATH))

REACT_PATH = os.path.abspath(os.path.join(WWW_PATH, "k-blog-react"))
DIST_PATH = os.path.abspath(os.path.join(REACT_PATH, "dist"))
STATIC_PATH = os.path.abspath(os.path.join(DIST_PATH, "static"))

# mongo config
MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_USERNAME = ""
MONGO_PWD = ""
MONGO_DBNAME = ""

# redis config
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379

try:
    from local_config import *
except Exception as e:
    print(e)

