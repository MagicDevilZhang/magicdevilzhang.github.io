---
layout: post
title: HUE集成FlinkSQL
permalink: /docs/数据开发/Hue/HUE集成FlinkSQL
---

# 配置Flink

通常Flink使用`TableAPI & SQL`
时候，注册的Catalog、Database以及Table都是以临时形式存储在内存中，当Job关闭后将丢失。为了在Hue中持久化集成FlinkSQL，我们需要对Flink增加HiveCatalog以支持持久化元数据存储。

## Hadoop环境

Apache Hive是基于Hadoop之上构建的, 首先您需要Hadoop的依赖:

```
export HADOOP_CLASSPATH=`hadoop classpath`
```

## 依赖包

要与Hive集成，您需要在Flink下的/lib/目录中添加一些额外的依赖包，以便通过Table API、SQL Client以及Flink SQL Gateway与Hive进行交互。

| Metastore Version | Dependency |
| ---- | ---- |
|1.0.0 - 1.2.2 | flink-sql-connector-hive-1.2.2 |
| 2.0.0 - 2.2.0 | flink-sql-connector-hive-2.2.0 |
|2.3.0 - 2.3.6 | flink-sql-connector-hive-2.3.6 |
| 3.0.0 - 3.1.2 | flink-sql-connector-hive-3.1.2 |

下载地址：https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-hive-2.2.0_2.11/1.13.0/

## 重启Flink

为了让包实时导入Flink，可以重启Flink集群

```
./bin/stop-cluster.sh
./bin/start-cluster.sh
```

# 配置Flink-SQL-Gateway

由于hue需要`Flink-SQL-Gateway`作为REST提供支持，所以需要下载配置此组件。

下载地址：https://github.com/ververica/flink-sql-gateway

## 配置Flink-SQL-Gateway **[关键]**

在Flink-SQL-Gateway的根目录下，修改配置文件`./conf/sql-gateway-defaults.yaml`文件：

```
catalogs:
  - name: myhive
    type: hive
    hive-conf-dir: /opt/cloudera/parcels/CDH/lib/hive/conf

execution:
  current-catalog: myhive
```

*如果需要对SQL-Client配置，也可以按照此方法修改Flink根目录下的`./conf/sql-client-defaults.yaml`文件*

## 启动Flink-SQL-Gateway

```
export FLINK_HOME=...
nohup ./bin/sql-gateway.sh &
```

# 配置Hue

Hue 4.8-4.9版本对FlinkSQL的支持仍在测试当中，可以打开Notebook2进行测试使用。

```
[notebook]
  enable_notebook_2=true

[[[flink]]]
  name=FlinkSQL
  interface=flink
  options='{"url": "http://FLINK_SQL_GATEWAY_HOST:8083"}'
```

# 参考链接

> - [FlinkSQL-Catalogs官方文档](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/table/catalogs/)
> - [FlinkSQL-Hive官方文档](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/connectors/table/hive/overview/)
> - [FlinkSQL-HiveCatalogs官方文档](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/connectors/table/hive/hive_catalog/)
> - [基于Flink 1.10版本的SQL演练](https://blog.csdn.net/qq_31866793/article/details/104422036)
> - [Flink集成Hive之快速入门](https://mp.weixin.qq.com/s/99ehmNzJVwW3cOrw_UkGsg)
> - [HUE连接FlinkSQL官方教程](https://gethue.com/blog/tutorial-query-live-data-stream-with-flink-sql/)