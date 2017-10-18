#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-10-13 下午2:52
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : myserver01.py
# @Software: PyCharm


# coding:utf-8

from wsgiref.simple_server import make_server


def RunServer(environ, start_response):
    # envision：客户端发来的所有数据
    # start_response:封装要韩会给用户的所有数据，包括响应头、状态码等
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']  # 获取客户端发来的数据中的url
    return ['<h1>Hello, web!</h1>'.encode('utf-8'), ]


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()