#!/usr/bin/env python
# coding:utf-8
from flask import Flask, send_from_directory, make_response
from urls.index import index_url
from urls.auth import auth_url
from urls.blog import blog_url

from config import STATIC_PATH, DIST_PATH

app = Flask(
    __name__,
    static_url_path="/static",
    static_folder=STATIC_PATH,
    template_folder=STATIC_PATH
)


@app.route('/app/<path:path>')
def app_handler(path):
    return send_from_directory(DIST_PATH, path)

index_url(app)
auth_url(app)
blog_url(app)
