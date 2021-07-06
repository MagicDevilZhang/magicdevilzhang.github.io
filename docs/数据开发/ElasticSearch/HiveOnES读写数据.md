---
layout: post
title: Hive On Elasticsearch读写数据
permalink: /docs/数据开发/ElasticSearch/HiveOnES读写数据
---



# 为Hadoop添加ES-Hadoop支持

1. 根据对应的ElasticSearch版本[下载ES-Hadoop包](https://www.elastic.co/downloads/past-releases#es-hadoop)；
2. 解压`elasticsearch-hadoop-xxxxx.zip`，并提取其中的`elasticsearch-hadoop-hive-xxxxx.jar`上传至HDFS中；
3. 在Hive命令行下执行`add jar hdfs:///jar/elasticsearch/elasticsearch-hadoop-hive-xxxxx.jar`添加此Jar包。

# 查看ElasticSearch的映射关系

可以在Kibana中使用Dev Tools通过执行下列代码查看某个索引的映社关系(mapping)：

```
GET /{YOUR_INDEX}/{TYPE}/_mapping?pretty
```

也可以在**Kibana=>Management=>Index Management=>{YOUR_INDEX}=>Mapping**查看映射关系。

以下给出一个查询后的mapping的样例：

```
GET company/_doc/_mapping?pretty
{
  "mappings": {
    "_doc": {
      "properties": {
        "id": {
          "type": "long"
        },
        "name": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "birth": {
          "type": "text"
        },
        "addr": {
          "type": "text"
        }
      }
    }
  }
}
```

# 在Hive中定义一个外表

```sql
add jar hdfs:///jar/elasticsearch/elasticsearch-hadoop-hive-6.8.16.jar;

DROP TABLE IF EXISTS octopus_fetch_test;

CREATE EXTERNAL table IF NOT EXISTS octopus_fetch_test( 
  `@timestamp`  timestamp,
  `@version`    STRING,
  `addr`        STRING,
  `areaid`      STRING,
  `areaname`    STRING,
  `birth`       STRING,
  `boxid`       STRING,
  `cells`       ARRAY<STRUCT<isChange:STRING,location:STRING,value:STRING>>,
  `createtime`  STRING,
  `dzqyid`      STRING,
  `dzqyname`    STRING,
  `fetchdatatime` BIGINT,
  `id`          STRING,
  `kjnd`        STRING,
  `kjqj`        STRING,
  `name`        STRING,
  `nsqxdm`      STRING,
  `parentboxid` STRING,
  `qyid`        STRING,
  `qyname`      STRING,
  `sbszid`      STRING,
  `sheetname`   STRING,
  `systemid`    STRING
)  
STORED BY 'org.elasticsearch.hadoop.hive.EsStorageHandler' 
TBLPROPERTIES(
    'es.nodes' = 'http://172.37.4.156',
    'es.port' = '9200',
    'es.net.ssl' = 'true', 
    'es.nodes.wan.only' = 'true', 
    'es.nodes.discovery'='false',
    'es.input.use.sliced.partitions'='false',
    'es.input.json' = 'false',
    'es.resource' = 'octopus_fetch-*/_doc',
    'es.net.http.auth.user' = 'elastic', 
    'es.net.http.auth.pass' = 'esadmin',
    'es.mapping.names' = 'areaid:areaId,areaname:areaName,boxid:boxId,createtime:createTime,dzqyid:dzQyId,dzqyname:dzQyName,fetchdatatime:fetchDataTime,parentboxid:parentBoxId,qyid:qyId,qyname:qyName,sbszid:sbszId,sheetname:sheetName,systemid:systemId'
);

SELECT * FROM octopus_fetch_test LIMIT 100;
```

其中，需要注意以下：

- 外表的结构根据在ES中查询到的映射结构(Mapping)定义的，在ES和Hive中类型的对应关系如下：

|  ES Type   |          Hive Type          |
| :--------: | :-------------------------: |
|  **null**  |          **void**           |
|  boolean   |           boolean           |
|  **byte**  |         **tinyint**         |
| **short**  |        **smallint**         |
|  **long**  |         **bigint**          |
|   double   |           double            |
|   float    |            float            |
|    int     |             int             |
| **string** | **string / varchar / char** |
|   binary   |           binary            |
|  **date**  |        **timestamp**        |
|  **map**   |      **struct / map**       |
|   array    |            array            |

- 需要重点注意的是，由于Hive表字段会自动转小写，而ES中字段是区分大小写的，因此直接查询会出现字段无法匹配的问题而查不到内容，因此需要特别指定`es.mapping.names`，它的格式是`'es.mapping.names':'hivekey:esKey[, ...]'`。

- 如果ES采用了加密，需要特别指示`'es.net.http.auth.user'='username'`和`'es.net.http.auth.user'='password'`用于指示用户名和密码。
- ES中的某个数组可以定义为Hive中的类型是`array<struct<name:type,...>>`。

# 参考连接

- [Aliyun Hive On ES 相关文档](https://help.aliyun.com/document_detail/184870.html?spm=a2c4g.11186623.6.831.44393382tqmZrz)

- [Hive On ES官方文档](https://www.elastic.co/guide/en/elasticsearch/hadoop/6.8/hive.html?spm=a2c4g.11186623.2.34.44393382tqmZrz)

- [Hive整和ES CSDN参考](https://blog.csdn.net/tototuzuoquan/article/details/102601040)
