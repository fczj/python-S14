#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-1 下午4:08
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : orm查询.py
# @Software: PyC

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.session import  sessionmaker



engine = create_engine("mysql+pymysql://root:mysql@127.0.0.1/school",
                       encoding='utf-8', echo=True)
Base = declarative_base() #生成orm基类
class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))



Session_class = sessionmaker(bind=engine)   # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()                   # 生成session实例


my_user = Session.query(User).filter_by(name="alex").first()

user_obj = User(name="alex", password="alex3714")   # 生成你要创建的数据对象
print(user_obj.name, user_obj.id)                   # 此时还没创建对象呢，不信你打印一下id发现还是None

print(Session.query(User.name,User.id).all() )      #获取所有数据

#objs = Session.query(User).filter(User.id>0).filter(User.id<7).all()   多条件查询