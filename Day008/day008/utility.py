#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-23 上午10:26
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : utility.py
# @Software: PyCharm

import hashlib
import os


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

