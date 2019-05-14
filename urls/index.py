#!/usr/bin/env python
# coding:utf-8
from views.index import IndexHandler, TestHandler


def index_url(app):
    app.add_url_rule('/', view_func=IndexHandler.as_view('index'))
    app.add_url_rule('/signin', view_func=IndexHandler.as_view('index-signin'))
    app.add_url_rule('/me', view_func=IndexHandler.as_view('index-me'))
    app.add_url_rule('/page/<bid>', view_func=IndexHandler.as_view('index-page'))

    app.add_url_rule('/admin', view_func=IndexHandler.as_view('index-admin'))
    app.add_url_rule('/write', view_func=IndexHandler.as_view('index-admin-write'))
    app.add_url_rule('/api/test', view_func=TestHandler.as_view('test'))
