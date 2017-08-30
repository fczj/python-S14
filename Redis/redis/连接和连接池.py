#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-30 下午4:54
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 连接和连接池.py
# @Software: PyCharm

import redis

r = redis.Redis(host='127.0.0.1', port=6379)
r.set('foo', 'Bar1')
print (r.get('foo'))