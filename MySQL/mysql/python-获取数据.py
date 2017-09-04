#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-1 下午3:26
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : python-获取数据.py
# @Software: PyCharm


import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql', db='school')
cursor = conn.cursor()
cursor.execute("select * from student")

# 获取第一行数据
row_1 = cursor.fetchone()

# 获取前n行数据
# row_2 = cursor.fetchmany(3)
# 获取所有数据
# row_3 = cursor.fetchall()

print(row_1)

conn.commit()
cursor.close()
conn.close()