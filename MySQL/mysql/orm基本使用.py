#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-1 下午3:46
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : orm基本使用.py
# @Software: PyCharm



import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.session import  sessionmaker


'''
#手动创建表
CREATE TABLE user (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(32),
    password VARCHAR(64),
    PRIMARY KEY (id)
)
'''



engine = create_engine("mysql+pymysql://root:mysql@127.0.0.1/school",
                       encoding='utf-8', echo=True)
#echo为true执行的是打印

Base = declarative_base() #生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


Base.metadata.create_all(engine)
# 创建表结构
#通过Base父类调用子类



#插入数据
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

user_obj = User(name="alex", password="alex3714")  # 生成你要创建的数据对象
print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None

Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
print(user_obj.name, user_obj.id)  # 此时也依然还没创建

Session.commit()  # 现此才统一提交，创建数据