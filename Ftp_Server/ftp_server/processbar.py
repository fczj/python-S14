#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-24 下午4:21
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : processbar.py
# @Software: PyCharm



from tqdm import tqdm
import os
import time

f = '/home/xiongzhibiao/ROOT.war'
size = os.stat(f).st_size

bar = tqdm(total=size,unit='bytes')
counter = 0
with open(f,'rb') as f:
    for i in iter(lambda :f.read(1000000),b''):
        counter += len(i)
        if counter < size:
            time.sleep(0.1)
            bar.update(1000000)


