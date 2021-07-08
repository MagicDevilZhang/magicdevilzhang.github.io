---
layout: post
title: HUE安装及部署
permalink: /docs/数据开发/Hue/HUE安装及部署
---

# 安装部署HUE

```shell
# Ubuntu 18.04 
# Python 2.7 + OpenJDK 11
# MySQL InnoDB Mysql-devel
# Node.js

# 获取源项目
# git clone https://github.com/cloudera/hue.git
# wget https://github.com.cnpmjs.org/cloudera/hue/archive/refs/heads/master.zip


# 安装：HUE依赖工具包
sudo apt-get install git ant gcc g++ libffi-dev libkrb5-dev libmysqlclient-dev libsasl2-dev libsasl2-modules-gssapi-mit libsqlite3-dev libssl-dev libxml2-dev libxslt-dev make maven libldap2-dev python-dev python-setuptools libgmp3-dev

# 问题：安装Node.js
# sudo apt-get install curl
# curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -
# sudo apt-get install -y nodejs


# 问题："my_config.h: No such file or directory" (https://issues.cloudera.org/browse/HUE-9390)
# sudo wget https://raw.githubusercontent.com/paulfitz/mysql-connector-c/master/include/my_config.h -O /usr/include/mysql/my_config.h


# 问题：Hue支持连接presto
# sudo ./build/env/bin/pip install pyhive

# 编译hue
sudo make apps


# 添加i18n国家化支持(https://docs.gethue.com/developer/development/#internationalization)
## desktop/core/src/desktop/setting.py
## ------------------------------------------------------
## LANGUAGE_CODE = 'zh-CN'    #LANGUAGE_CODE = 'en-us'
## LANGUAGES = [
##   ('zh-CN', _('Simplified Chinese')),
## ]
## ------------------------------------------------------
# sudo ./build/env/bin/pybabel init -D django -i ./desktop/core/src/desktop/locale/zh_CN/LC_MESSAGES/django.po -d . -l fr
sudo make locales

# 初始化服务
sudo ./build/env/bin/hue migrate

# 启动服务
sudo ./build/env/bin/hue runserver

# 启动外网访问
sudo ./build/env/bin/hue runserver 0.0.0.0:8000
```

# 部署

## HUE数据库配置

# 问题

## 查看用户查询次数

```sql
select
    user.id as id,
    user.username as username,
    document.extra as notebook,
    count(document.id) as cnt
from
    hue.auth_user as user left outer join hue.desktop_document as document
    on user.id = document.owner_id
where
    document.last_modified > '2021-01-01'
group by user.id,user.username,document.extra
order by cnt desc;
```



# 参考链接

> - [HUE官方使用手册](https://docs.gethue.com/)
