---
layout: post
title: MongoDB安装
permalink: /docs/数据开发/MongoDB/MongoDB安装
---

# 安装MongoDB

- [下载解压](https://www.mongodb.com/try/download/community)

```
# Ubuntu 18.04 LTS ("Bionic")/Debian 10 "Buster"：
sudo apt-get install libcurl4 openssl

#Ubuntu 16.04 LTS ("Xenial")/Debian 9 "Stretch"：
sudo apt-get install libcurl3 openssl

wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-4.2.8.tgz
```

- 建立软连接并导入PATH

```
link -r /opt/mongodb  /usr/local/mongodb
export PATH=/usr/local/mongodb/bin:$PATH
```

- 创建数据库目录

```
# 数据存储目录：/var/lib/mongodb
# 日志文件目录：/var/log/mongodb
sudo mkdir -p /var/lib/mongo
sudo mkdir -p /var/log/mongodb
sudo chown yzf /var/lib/mongo     # 设置权限
sudo chown yzf /var/log/mongodb   # 设置权限
```

- 启动 MongoDB 服务

```
/opt/mongodb/bin/mongod --dbpath /var/lib/mongo --logpath /var/log/mongodb/mongod.log  --bind_ip=0.0.0.0 --fork
/opt/mongodb/bin/mongod --dbpath /var/lib/mongo --logpath /var/log/mongodb/mongod.log --shutdown
```

# 参考链接

> - [MongoDB官方使用手册](https://docs.mongodb.com/manual/administration/install-community/)
