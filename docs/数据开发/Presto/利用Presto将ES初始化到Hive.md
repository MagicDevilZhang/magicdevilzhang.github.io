---
layout: post
title: 利用Presto将ES初始化到Hive
permalink: /docs/数据开发/Presto/利用Presto将ES初始化到Hive
---

# Presto连接ElasticSearch

在ElasticSearch开启**外网访问**后，可在Presto中配置连接ES:

- 在Presto根目录下新增`./etc/catalog/elasticsearch.properties`

```
connector.name=elasticsearch
elasticsearch.host=localhost
elasticsearch.port=9200
elasticsearch.default-schema-name=default
```

其他配置详见[Trino Docs](https://trino.io/docs/current/connector/elasticsearch.html#configuration-properties)

其中需要注意的是，Presto中`Schema`概念对应的是ES中的`Index`.

- 为ElasticSearch增加Array支持 **[关键]**

Presto无法自动识别ElasticSearch中的数组元素，如`cells`。因此需要在ElasticSearch中对某个`Index`配置其`Mapping`映射关系。

```
curl -H 'Content-Type: application/json' -XPOST 'http://elasticsearch:9200/index/type/_mapping' -d'
{
    "_meta": {
        "presto":{
            "cells":{
                "isArray":true
            }
        }
    },
    "properties": {
        ...
    }
}'
```

- 在使用Presto连接ES时，如果遇到连接失败，可以访问ES配置查看详细网络环境：

```
http://172.37.4.155:9200/_nodes?pretty
```

```
{
  "nodes": {
    "qN3fa_tdRtCKuAv2xGhxxQ": {
      "name": "qN3fa_t",
      "transport_address": "127.0.0.1:9300",
      "host": "127.0.0.1",
      "ip": "127.0.0.1",
      "version": "6.5.4"
    }
  }
}
```

# Presto连接Hive

- 在Presto根目录下新增`./etc/catalog/hive.properties`

```
connector.name=hive-hadoop2
hive.metastore.uri=thrift://172.24.10.2:9083
```

- Presto使用Hive时，如果出现问题如下：

```
java.net.UnknownHostException: master.prd.yzf
```

则可以在客户机`/etc/hosts`添加Hosts信息。

```
172.24.10.2    master.prd.yzf
```

# ES初始化到Hive

- 配置完ES和Hive的Catalogs后，重启Presto：

```
./bin/launcher restart &
```

- 使用客户端连接Presto

```
java -jar presto-cli.jar --server localhost:8880
```

- 初始ES到Hive中

```
# SHOW CATALOGS;
# SHOW SCHEMAS FROM elasticsearch;
# SHOW TABLES FROM elasticsearch.default;

# 追加数据
# INSERT INTO hive.es_database.octopus_test
#  SELECT COUNT(*) FROM elasticsearch.default.octopus WHERE ...;

CREATE TABLE hive.es_database.octopus_test WITH ( format = 'parquet' ) AS 
  SELECT COUNT(*) FROM elasticsearch.default.octopus;
```

- 查看初始化结果

```
DESC hive.es_database.octopus_test;
SELECT * FROM hive.es_database.octopus_test;

# 含有数组
SELECT * FROM (
  SELECT t.*, c.`ischange`, c.`value`, c.`location`
  FROM 
    es_database.octopus_test AS t
    LATERAL VIEW explode(cells) tab AS c
) a;
```

Column|    Type 
---------------|---------------------------------------------------------------|
@timestamp    | timestamp||
@version      | varchar||
areaid        | varchar||
areaname      | varchar||
boxid         | varchar||
**cells**     | **array(row(ischange varchar, location varchar, value varchar))**||
createtime    | varchar||
dzqyid        | varchar||
dzqyname      | varchar||
fetchdatatime | bigint||
id            | varchar||
kjnd          | varchar||
kjqj          | varchar||
nsqxdm        | varchar||
parentboxid   | varchar||
qyid          | varchar||
qyname        | varchar||
sbszid        | varchar||
sheetname     | varchar||
systemid      | varchar||

# 参考连接

- [Trino ES Connector](https://trino.io/docs/current/connector/elasticsearch.html)