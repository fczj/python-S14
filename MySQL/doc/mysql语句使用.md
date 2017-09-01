[参考](http://www.cnblogs.com/alex3714/articles/5950372.html)
[mysql-学习系列](http://www.zsythink.net/archives/category/%E5%AD%98%E5%82%A8/mariadb/page/4/)
[w3c](http://www.w3school.com.cn/sql/index.asp)


## 查看帮助

```
mysql> \h create database
```

## 数据库和表创建
### 数据库
1.创建并设置字符集
```
CREATE DATABASE IF NOT EXISTS school CHARACTER SET = utf8 COLLATE = utf8_general_ci;
```

2.查看所有字符集
```
SHOW CHARACTER SET;
```

### 创建表
```
create table student(
   stu_id INT NOT NULL AUTO_INCREMENT,
   name CHAR(32) NOT NULL,
   age  INT NOT NULL,
   register_date DATE,
   PRIMARY KEY ( stu_id )
);
```

## 常用语句
### 查询
```
select * from student where register_date > '2016-03-04';
select * from student limit 3 offset 2;
```


### 插入
```
insert into student (name,age,register_date) values ("alex li",22,"2016-03-4");
```

### 更新
```
update student set age=22 ,name="Alex Li" where stu_id>3;
```

### 排序
```
使用 ASC 或 DESC 关键字来设置查询结果是按升序或降序排列。 默认情况下，它是按升序排列。
select *from student where name like binary "%Li" order by stu_id desc;
```

### 分组
```
使用 WITH ROLLUP
mysql> SELECT name, SUM(singin) as singin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;
```


### 修改表属性
1.删除字段
```
alter table student drop register_date; 
#从student表删除register_date   字段
```

2.添加字段
```
alter table student add phone int(11) not null; 
＃添加phone字段
```

3.修改字段属性
```
ALTER TABLE testalter_tbl MODIFY j BIGINT NOT NULL DEFAULT 100;
```

4.修改表名
```
ALTER TABLE testalter_tbl RENAME TO alter_tbl;
```


### mysql外键约束和级联
[w3c](http://www.w3school.com.cn/sql/index.asp)

1.创建外建依赖的两个表
```
create table dage(
id int(4) not null auto_increment,
name varchar(11) not null,
primary key (id)
);

create table xiaodi(
id int(4) not null auto_increment,
dage_id int(4) not null,
name varchar(11),
primary key(id),
FOREIGN KEY (dage_id) REFERENCES dage(id)                                                                                
);

```

2.插入-大哥没有的时候不能创建小弟
```
mysql> insert into dage values(1,'laoda');
Query OK, 1 row affected (0.04 sec)

mysql> insert into xiaodi values(1,2,'xiaodi');
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`school`.`xiaodi`, CONSTRAINT `xiaodi_ibfk_1` FOREIGN KEY (`dage_id`) REFERENCES `dage` (`id`))
mysql> 
mysql> insert into xiaodi values(1,1,'xiaodi');
Query OK, 1 row affected (0.02 sec)

```

3.小弟还在大哥不能随便删除
```
mysql> delete from dage;
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`school`.`xiaodi`, CONSTRAINT `xiaodi_ibfk_1` FOREIGN KEY (`dage_id`) REFERENCES `dage` (`id`))
```
