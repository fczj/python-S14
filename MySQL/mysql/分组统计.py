#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-1 下午4:44
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 分组统计.py
# @Software: PyCharm


Session.query(User).filter(User.name.like("Ra%")).count()

#使用sqlalcchemy
from sqlalchemy import func
print(Session.query(func.count(User.name),User.name).group_by(User.name).all() )

#相当于这个语句
SELECT count(user.name) AS count_1, user.name AS user_name
FROM user GROUP BY user.name