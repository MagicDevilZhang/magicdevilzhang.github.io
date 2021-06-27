---
layout: post
title: Kafka安装及配置
permalink: /docs/数据开发/Kafka/Kafka安装与配置
---

# 单机测试Kafka安装

## 下载安装Kafka

```
wget https://downloads.apache.org/kafka/2.8.0/kafka_2.12-2.8.0.tgz
tar -zxvf kafka_2.12-2.8.0.tgz
```

## 单机ZooKeeper

Kafka需要依赖ZooKeeper做集群管理，因此需要首先配置ZooKeeper。若需要单机测试，可直接运行Kafka自带的ZooKeeper运行。

```
./bin/zookeeper-server-start.sh ./config/zookeeper.properties
```

## 配置Kafka

修改Kafka根目录下的`./config/server.properties`文件

```
broker.id=0 #各个节点应当有不同的id对应
listeners=PLAINTEXT://192.168.68.121:9092 #当前节点的地址及端口
zookeeper.connect=localhost:2181 #设置ZooKeeper的地址和端口，多个节点用分号隔开
```

## 启动Kafka

```
./bin/kafka-server-start.sh ./config/server.properties 
```

## 建立Topic

```
./bin/kafka-topics.sh --create --topic demo-topic --bootstrap-server 192.168.68.121:9092[,...]
./bin/kafka-topics.sh --list --bootstrap-server 192.168.68.121:9092[,...]
```

## 删除Topic

```
./bin/kafka-topic.sh --delete --topic demo-topic --bootstrap-server 192.168.68.121:2181[,...]
```

# 多集群配置Kafka

同但集群配置，需要注意的是:

1. ZooKeeper最好使用单独的集群，且Kafka节点配置相同的ZooKeeper地址;
2. 各节点`server.properties`配置中的`broker.id`必须不同。

# Docker配置Kafka集群

```
# docker直接拉取kafka和zookeeper的镜像
docker pull wurstmeister/kafka
docker pull wurstmeister/zookeeper 

# 首先需要启动zookeeper，如果不先启动，启动kafka没有地方注册消息
docker run -it --name zookeeper -p 2181:2181 -d wurstmeister/zookeeper:latest

# 启动kafka容器，注意需要启动三台,注意端口的映射，都是映射到9092

# 第一台
docker run -it --name kafka01 -p 9092:9092 -d -e KAFKA_BROKER_ID=0 -e KAFKA_ZOOKEEPER_CONNECT=192.168.68.121:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.68.121:9092 -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 wurstmeister/kafka:latest

# 第二台
docker run -it --name kafka02 -p 9093:9092 -d -e KAFKA_BROKER_ID=1 -e KAFKA_ZOOKEEPER_CONNECT=192.168.68.121:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.68.121:9093 -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 wurstmeister/kafka:latest

# 第三台
docker run -it --name kafka03 -p 9094:9092 -d -e KAFKA_BROKER_ID=2 -e KAFKA_ZOOKEEPER_CONNECT=192.168.68.121:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.68.121:9094 -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 wurstmeister/kafka:latest
```

# 参考链接

> - [Kafka Quick Start](http://kafka.apache.org/quickstart)
> - [Kafka说明书](https://blog.csdn.net/cao1315020626/article/details/112590786)
