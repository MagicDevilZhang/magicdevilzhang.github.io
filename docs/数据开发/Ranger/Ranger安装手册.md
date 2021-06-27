---
layout: post
title: Ranger安装手册
permalink: /docs/数据开发/Ranger/Ranger安装手册
---

# 下载编译Ranger

Ranger没有提供编译好的二进制安装包，需要自行下载并使用maven进行编译。

- 安装环境

```
Ubuntu 18.04
JDK8
Maven3.6.0
Python 2.7（Python3可能报错）
MySQL 5.1
```

- 下载安装Ranger，并将解压到/opt/ranger下，本文档基于2.0.0版本

```
sudo wget https://downloads.apache.org/ranger/2.0.0/apache-ranger-2.0.0.tar.gz
```

- 修改pom.xml的maven和jdk版本

```
sudo vim /opt/ranger/pom.xml
```

```
<maven.version.required>3.6.0</maven.version.required>
<java.version.required>1.8</java.version.required>
<javac.source.version>1.8</javac.source.version>
<javac.target.version>1.8</javac.target.version>
```

- 编译：使用mvn进行编译时间较长，可以在mvn添加多线程参数，编译后的文件保存在`./target`目录下。

```
sudo mvn clean compile package assembly:assembly install -DskipTests -Drat.skip=true -T 3
```

# 安装Ranger-Admin组件

Ranger-Admin是一个基于Web的可视化界面，也是Ranger的权限授权主机。

- 解压Ranger-Admin组件

```
sudo tar -zxvf ./target/ranger-2.0.0-admin.tar.gz
```

- 修改`install.properties`配置

```
sudo vim ./target/ranger-2.0.0-admin/install.properties
```

```
# 确保mysql connector已配置，没有的话去官网下载
SQL_CONNECTOR_JAR=/usr/share/java/mysql-connector-java.jar

# mysql root用户、密码、主机
db_root_user=root
db_root_password=password
db_host=localhost

#Ranger会建立一个ranger的数据库和用户，建议手动创建
db_name=ranger
db_user=ranger
db_password=rangeradmin

# admin 的url
policymgr_external_url=http://localhost:6080
policymgr_http_enabled=true
policymgr_https_keystore_file=
policymgr_https_keystore_keyalias=rangeradmin
policymgr_https_keystore_password=rangeradmin

#audit审计文件配置，设置为空表示不启动审计
audit_store=
```

- 手动配置Ranger数据库（可选）

```sql
# 登录MySQL数据 mysql -h localhost -u root -p
create database ranger;
create user 'ranger'@'localhost' identified by 'rangeradmin';
create user 'ranger'@'%' identified by 'rangeradmin';
grant all privileges on ranger.* to ranger@'localhost' identified by 'rangeradmin';
grant all privileges on ranger.* to ranger@'%' identified by 'rangeradmin';
flush privileges;
```

- 安装并运行Ranger-Admin

1. 如果没有配置JAVA_HOME: `export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64`
2.
若安装时出现数据库问题，可以以ranger用户登录mysql手动刷sql脚本，查看具体出错位置并配置数据库：`/opt/ranger/target/ranger-2.0.0-admin/db/mysql/optimized/current/ranger_core_db_mysql.sql`

```
sudo ./target/ranger-2.0.0-admin/setup.sh
sudo ./target/ranger-2.0.0-admin/ews/ranger-admin-services.sh start
sudo ./target/ranger-2.0.0-admin/ews/ranger-admin-services.sh stop
```

# 安装Ranger-Usersync组件

Ranger-usersync是用户同步插件，支持从unix系统或者LDAP中同步用户到ranger中进行权限管控。

- 解压Ranger-Usersync组件

```
sudo tar -zxvf ./target/ranger-2.0.0-usersync.tar.gz
```

- 修改`install.properties`配置

```
sudo vim ./target/ranger-2.0.0-usersync/install.properties
```

```
#配置ranger admin的地址
POLICY_MGR_URL = http://localhost:6080

#同步源系统类型
SYNC_SOURCE = unix

#同步间隔时间 单位分钟 unix默认5 ldap 默认360
SYNC_INTERVAL = 5

#usersync程序运行的用户和用户组
unix_user=ranger
unix_group=ranger

#修改rangerusersync用户的密码。注意，此密码应与Ranger admin中install.properties的rangerusersync_password相同。
rangerUsersync_password=
```

- 安装并启动

```
# export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
sudo ./target/ranger-2.0.0-usersync/setup.sh
sudo ./target/ranger-2.0.0-usersync/ranger-usersync-services.sh start
```

# 安装Ranger-Presto组件

注意，Ranger2.0.0仅仅支持PrestoSQL,后续更名的Trino由于java接口命名修改，Ranger暂时不兼容Trino，此处使用的是[PrestoSQL332](https://repo1.maven.org/maven2/io/prestosql/presto-server/332/presto-server-332.tar.gz)。

- 解压Ranger-Presto组件

```
sudo tar -zxvf ./target/ranger-2.0.0-presto.tar.gz
```

- 修改`install.properties`配置

```
sudo vim ./target/ranger-2.0.0-presto/install.properties
```

```
#配置ranger admin的地址
POLICY_MGR_URL = http://localhost:6080

#配置Ranger配置名称（和RangerAdminUI中命名必须一致）
REPOSITORY_NAME=prestodev

#配置presto的路径地址
COMPONENT_INSTALL_DIR_NAME=/opt/presto/

#为了简单，此处不开启审计功能
XAAUDIT.SOLR.ENABLE=false

#此处手动添加该配置
XAAUDIT.SUMMARY.ENABLE=false
```

- 启动前请先关闭Presto进程

```
# export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
sudo ./enable-presto-plugin.sh
sudo ./enable-presto-plugin.sh
```

- 在Ranger中配置Presto后，再启动Presto

# 参考链接

> - [Apache Raner官网](https://ranger.apache.org/)
> - [Apache Ranger 安装部署](https://www.yuque.com/u552836/rospxv/ehz3lg)
> - [Ranger Admin/Plugins 安装](https://www.jianshu.com/p/888186c38827)
> - [Ranger安装部署](Ranger安装部署)
> - [Ranger安装部署到使用测试（踩坑详情）](https://blog.csdn.net/weixin_38586230/article/details/105725346)
