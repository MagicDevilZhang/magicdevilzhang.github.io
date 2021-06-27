---
layout: post
title: MySQL手动安装
permalink: /docs/数据开发/MySQL/MySQL手动安装
---

> - [MySQL历史版本下载](https://downloads.mysql.com/archives/community/)
> - [MySQL8.0官方安装手册](https://dev.mysql.com/doc/refman/8.0/en/binary-installation.html)

- 在`/opt`中解压缩

```
sudo wget https://downloads.mysql.com/archives/get/p/23/file/mysql-5.1.48-linux-x86_64-icc-glibc23.tar.gz
sudo tar -zxvf mysql-5.1.48-linux-x86_64-icc-glibc23.tar.gz
```

- 创建mysql用户组,建立mysql用户并加入mysql用户组

```
sudo groupadd mysql
sudo useradd mysql -g mysql -p mysqladmin -s /sbin/nologin -M
# -g 是加入到mysql用户组，-p是设置密码，-s是设置shell，这里设置的是不让其登录，-M就是不建立用户目录。
```

- 建立软连接并初始化：

```
sudo ln -s /opt/mysql /usr/local/mysql
sudo chgrp -R mysql /opt/mysql
sudo chgrp -R mysql /opt/mysql/data
sudo chgrp -R mysql /usr/local/mysql
sudo chgrp -R mysql /usr/local/mysql/data
sudo scripts/mysql_install_db --user=mysql
```

- 添加到系统环境

```
sudo vim ~/.bashrc
```

```
export MYSQL_HOME=/usr/local/mysql
export PATH=$PATH:$MYSQL_HOME/bin
```

```
source ~/.bashrc
```

```
sudo cp /opt/mysql/support-files/my-medium.cnf /etc/my.cnf
sudo cp /opt/mysql/support-files/mysql.server /etc/init.d/mysqld
sudo /etc/init.d/mysqld start
sudo /etc/init.d/mysqld status
```

- 给mysql的`root`用户指定密码为`mysqladmin`,host为`localhost` ，如下：

```
sudo /opt/mysql/bin/mysqladmin -u root password 'mysqladmin'
```

- 启动使用MySQL

```
mysql -h localhost -u root -p mysqladmin
```