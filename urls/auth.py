#!/usr/bin/env python
# coding:utf-8
from views.auth import AuthHandler, LoginHandler,LoginOutHandler


def auth_url(app):
    app.add_url_rule('/api/auth', view_func=AuthHandler.as_view('auth'))
    app.add_url_rule('/api/login', view_func=LoginHandler.as_view('auth-login'))
    app.add_url_rule('/api/signin', view_func=LoginHandler.as_view('auth-signin'))
    app.add_url_rule('/api/signout', view_func=LoginOutHandler.as_view('auth-signout'))
