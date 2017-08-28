#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-28 下午3:17
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 协程爬虫.py
# @Software: PyCharm

import sys
sys.path.append('/home/xiongzhibiao/github/python-S14/Common/common')

from gevent import monkey;monkey.patch_all()
import gevent
import requests
from utility import run_time


f = open('/tmp/spider1','w')

# @run_time
def spider(url):
    a= requests.get(url).text
    f.write(a)



@run_time
def xiecheng(lst):
    gevent_lst = [gevent.spawn(spider, url) for url in url_lst]
    gevent.joinall(gevent_lst)


@run_time
def chuangxing(lst):
    for url in lst:
        spider(url)


url_lst = [
    'http://news.cctv.com/2017/08/27/ARTIwhbfJpb1Y39T0jOrMu3h170827.shtml',
    'http://news.cctv.com/2017/08/28/ARTI3HQUoS5zxPidtg4QcPWt170828.shtml',
    'http://news.xinhuanet.com/politics/2017-08/27/c_1121550305.htm',
    'http://www.sina.com.cn/',
    'http://news.sina.com.cn/world/',
    'http://sports.sina.com.cn/'
]

# xiecheng(url_lst)                 #0.1秒
chuangxing(url_lst)                 #0.4秒

f.close()

'''
总结:
1.使用gevent的时候必须执行from gevent import monkey;monkey.patch_all()
否则gevent不能识别request是阻塞操作

'''

