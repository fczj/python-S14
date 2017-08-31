## 安装
```
docker pull mysql:5.6
```

```
docker run -p 3306:3306 --name mymysql \
    -v $PWD/conf/my.cnf:/etc/mysql/my.cnf \
    -v $PWD/logs:/logs \
    -v $PWD/data:/mysql_data \
    -e MYSQL_ROOT_PASSWORD=123456 
    -d mysql:5.6
 
sudo docker run \
--name mymysql \
-p 3306:3306 \
-v /home/xiongzhibiao/github/python-S14/MySQL/data:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=mysql \
-d mysql:latest
```

```
sudo docker ps |grep mysql
```


```angular2html
mysql -uroot -p -h 127.0.0.1 -P 3306 -p
```

