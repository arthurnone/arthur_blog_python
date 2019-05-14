#!/usr/bin/env python
# coding:utf-8
from __future__ import print_function
from .base import BaseMongoDB


class Blog(BaseMongoDB):
    collection_name = "blog"
    keys = ["_id", "title", "body", 'type', 'tag', 'language', 'author', 'uid', 'create_time', 'update_time']
