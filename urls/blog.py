#!/usr/bin/env python
# coding:utf-8
from views.blog import BlogHandler


def blog_url(app):
    app.add_url_rule('/api/blog', view_func=BlogHandler.as_view('api-blog'))
