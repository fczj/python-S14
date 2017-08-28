#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-27 下午3:57
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : xiaoliang.py
# @Software: PyCharm

import re
import requests



def zong(key,url):
    text = requests.get(url).text
    xiao = re.compile('{}')