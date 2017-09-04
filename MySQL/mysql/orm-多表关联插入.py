#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-4 下午10:21
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : orm-多表关联插入.py
# @Software: PyCharm

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DATE
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:mysql@127.0.0.1/school",
                       encoding="utf-8")
Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=True)
    register_date = Column(DATE, nullable=True)

    # 加个关联关系
    def __repr__(self):
        return "<%s name:%s>" % (self.id, self.name)


class StudyRecord(Base):
    __tablename__ = "StudyRecord"
    id = Column(Integer, primary_key=True, autoincrement=True)
    day = Column(Integer)
    status = Column(String(32))
    stu_id = Column(Integer, ForeignKey(Student.id))
    # 加个关联关系
    student = relationship("Student", backref="my_study_record")
    #在StudyRecord中可以通过my_study_record字段反查Student中的所有字段

    def __repr__(self):
        return "<%s day:%s status:%s>" % (self.student.name, self.day, self.status)


Session_class = sessionmaker(bind=engine) #创建与数据库的会话session class,注意这里返回给session的是个类，不是实例
session = Session_class() #生成session实例

# ret = session.query(Student).join(StudyRecord).all()  #这种方式需要主外键关联
# print(ret)
#
# # ret = session.query(Student,StudyRecord).filter(Student.id==StudyRecord.stu_id).all()
# # print(ret)
#
# s1 = Student(name="Alex",register_date='2013-02-01')
# s2 = Student(name="Jack",register_date='2014-04-01')
# s3 = Student(name="gao",register_date='2013-10-01')
# s4 = Student(name="wang",register_date='2011-11-01')
#
# study_obj1 = StudyRecord(day=1,status="YES",stu_id=1)
# study_obj2 = StudyRecord(day=2,status="NO",stu_id=1)
# study_obj3 = StudyRecord(day=3,status="YES",stu_id=1)
# study_obj4 = StudyRecord(day=1,status="YES",stu_id=2)
# #
# session.add_all([s1,s2,s3,s4,study_obj1,study_obj2,study_obj3,study_obj4])
# session.commit()

# 查出Alex上了几节课
stu_obj = session.query(Student).filter(Student.name == 'Alex').first()
print(stu_obj.my_study_record)
