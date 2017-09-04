#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-4 下午9:55
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : orm-多表外键关联.py
# @Software: PyCharm

'''
参考：http://www.cnblogs.com/guqing/p/6653843.html
'''


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


Base.metadata.create_all(engine)  # 创建表结构

latin_ = '''
学生表
mysql> desc student;
+---------------+-------------+------+-----+---------+----------------+
| Field         | Type        | Null | Key | Default | Extra          |
+---------------+-------------+------+-----+---------+----------------+
| id            | int(11)     | NO   | PRI | NULL    | auto_increment |
| name          | varchar(32) | YES  |     | NULL    |                |
| register_date | date        | YES  |     | NULL    |                |
+---------------+-------------+------+-----+---------+----------------+
| student | CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `register_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |


记录表，外键依赖student的id
mysql> desc StudyRecord;                                                           
+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| id     | int(11)     | NO   | PRI | NULL    | auto_increment |
| day    | int(11)     | YES  |     | NULL    |                |
| status | varchar(32) | YES  |     | NULL    |                |
| stu_id | int(11)     | YES  | MUL | NULL    |                |
+--------+-------------+------+-----+---------+----------------+

| StudyRecord | CREATE TABLE `StudyRecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `day` int(11) DEFAULT NULL,
  `status` varchar(32) DEFAULT NULL,
  `stu_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `stu_id` (`stu_id`),
  CONSTRAINT `StudyRecord_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |



'''
