---
layout: post
title: Elasticsearch安装与部署
permalink: /docs/数据开发/ElasticSearch/Elasticsearch安装与部署
---

# 安装Elasticsearch

- 前往[官方下载页面](https://www.elastic.co/cn/downloads/past-releases#elasticsearch)下载所需版本的Elasticsearch，以6.8.16版本为例安装Elasticsearch：

```
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.8.16.tar.gz
tar -zxvf elasticsearch-6.8.16.tar.gz
```

- 配置Elasticsearch：

```
vim ./config/elasticsearch.yml
```

```
# 节点名称和机架
node.name: es-master
node.attr.rack: r1

# 外网访问
network.host: 0.0.0.0
http.port: 9200

# 密码验证
http.cors.enabled: true
http.cors.allow-origin: "*"
http.cors.allow-headers: Authorization
xpack.security.enabled: true
xpack.security.transport.ssl.enabled: true
```

- 运行启动并设置账号密码

```
nohup ./bin/elasticsearch &
./bin/elasticsearch-setup-passwords
```

# 安装Kibana

- 前往[官方下载页面](https://www.elastic.co/cn/downloads/past-releases#kibana)下载所需版本的Kibana，以6.8.16版本为例安装Kibana：

```
wget https://artifacts.elastic.co/downloads/kibana/kibana-6.8.16-linux-x86_64.tar.gz
tar -zxvf kibana-6.8.16-linux-x86_64.tar.gz
```

- 配置Kibana：

```
vim ./config/kibana.yml
```

```
# 配置外网访问
server.port: 5601
server.host: "0.0.0.0"

# 配置Elasticsearch地址
elasticsearch.hosts: ["http://0.0.0.0:9200"]

# 配置账号密码
elasticsearch.username: "elastic"
elasticsearch.password: "esadmin"
```

- 启动并运行

```
nohup ./bin/kibana &
```

