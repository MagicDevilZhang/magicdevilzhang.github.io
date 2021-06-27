---
layout: post
title: Presto安装及部署
permalink: /docs/数据开发/Presto/Presto安装及部署
---

# Presto安装及部署

- 获取Presto

```
sudo wget https://repo1.maven.org/maven2/io/prestosql/presto-server/332/presto-server-332.tar.gz
sudo tar -zxvf presto-server-332.tar.gz
```

- 配置Node

```
sudo vim etc/node.properties
```

```
node.environment=production
node.id=ffffffff-ffff-ffff-ffff-ffffffffffff
node.data-dir=data
```

- 配置JVM虚拟机

```
sudo vim etc/jvm.config
```

```
-server
-Xmx16G
-XX:-UseBiasedLocking
-XX:+UseG1GC
-XX:G1HeapRegionSize=32M
-XX:+ExplicitGCInvokesConcurrent
-XX:+ExitOnOutOfMemoryError
-XX:+HeapDumpOnOutOfMemoryError
-XX:ReservedCodeCacheSize=512M
-XX:PerMethodRecompilationCutoff=10000
-XX:PerBytecodeRecompilationCutoff=10000
-Djdk.attach.allowAttachSelf=true
-Djdk.nio.maxCachedBufferSize=2000000
# -Dpresto-temporarily-allow-java8=true
```

- 配置单机环境的Config

```
sudo vim etc/config.properties
```

```
coordinator=true
node-scheduler.include-coordinator=true
http-server.http.port=8880
query.max-memory=2GB
query.max-memory-per-node=1GB
query.max-total-memory-per-node=2GB
discovery-server.enabled=true
discovery.uri=http://localhost:8880
```

- 配置Log日志

```
sudo vim etc/log.properties
```

```
io.presto=INFO
```

- 配置catalog连接

```
sudo vim etc/catalog/mysql.properties
```

```
connector.name=mysql
connection-url=jdbc:mysql://localhost:3306
connection-user=root
connection-password=mysqladmin
```

# 参考链接

> - [Trino官方安装手册](https://trino.io/docs/current/installation/deployment.html)
> - [PrestoDB官方安装手册](https://prestodb.io/docs/current/installation/deployment.html)
