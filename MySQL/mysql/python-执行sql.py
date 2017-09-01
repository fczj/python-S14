#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-1 下午3:17
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : python-执行sql.py
# @Software: PyCharm


import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql', db='school')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("insert into student values(6,'zhi',24,'2017-01-01')")

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

# 执行SQL，并返回受影响行数
# effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])


# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()