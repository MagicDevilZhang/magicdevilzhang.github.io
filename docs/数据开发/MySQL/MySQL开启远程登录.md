---
layout: post
title: MySQL开启远程登录
permalink: /docs/数据开发/MySQL/MySQL开启远程登录
---

# MySQL开启远程登录

- 登录MySQL

```
mysql -h localhost -u root -p mysqladmin
```

- 授权root用户登录权限

```sql
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'mysqladmin' WITH GRANT OPTION; 
FLUSH PRIVILEGES; 
SELECT host,user,password FROM mysql.user;
```

# 对于MySQL5.5以上版本可能存在的问题（可选）

以上操作可能失效，尝试如下方法：

- MySQL配置文件

```
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
```

- 设置MySQL用户登录验证器

```sql
update mysql.user set authentication_string=PASSWORD('mysqladmin'), plugin='mysql_native_password' where user='root';
```

- 设置密码等级

```sql
SHOW VARIABLES LIKE 'validate_password%';
SET GLOBAL validate_password_policy=0;
```