#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-1 下午4:13
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : orm修改.py
# @Software: PyCharm

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.session import  sessionmaker



engine = create_engine("mysql+pymysql://root:mysql@127.0.0.1/school",
                       encoding='utf-8')
Base = declarative_base() #生成orm基类
class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(32))
    password = Column(String(64))



Session_class = sessionmaker(bind=engine)   # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()                   # 生成session实例


my_user = Session.query(User).filter_by(name="Alex Li").first()
my_user.name = "chenshifei"
Session.commit()
