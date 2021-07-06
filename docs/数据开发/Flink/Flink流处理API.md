---
layout: post
title: Flink流处理API
permalink: /docs/数据开发/Flink/Flink流处理API
---

# Environment

对于Bounded有界流数据，可以采用`ExecutionEnvironment`创建执行环境；对于Unbounded无界流数据，可以采用`StreamExecutionEnvironment`创建。具体创建方法如下：

```java
StreamExecutionEnvironment.createLocalEnvironment(parralism);
```

```java
StreamExecutionEnvironment.createRemoteEnvironment(hostname,port,jars);
```

```java
StreamExecutionEnvironment.getExecutionEnvironment(); // 自动识别当前执行环境并实例化执行环境对象【推荐】
```

# Source

## 从集合中读取数据

```java
        DataStream<Tuple2> input = env.fromCollection(Arrays.asList(
                new Tuple2(1, "hello"),
                new Tuple2(2, "world"),
                new Tuple2(3, "hello"),
                new Tuple2(4, "flink")
        ));
```

```java
        DataStream<Tuple2> input = env.fromElements(
                new Tuple2(1, "hello"),
                new Tuple2(2, "world"),
                new Tuple2(3, "hello"),
                new Tuple2(4, "flink")
        );
```

## 从文件读取数据

```java
        env.readFile(new FileInputFormat<Object>() {
            @Override
            public boolean reachedEnd() throws IOException { return false; }
            @Override
            public Object nextRecord(Object reuse) throws IOException { return null; }
        },FILE_PATH);
```

```java
        env.readTextFile(FILE_PATH, CHAR_SET)
```

## 从Kafka读取数据

- 引入flink-connector-kafka组件

```xml
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-connector-kafka_${scala.version}</artifactId>
            <version>${flink.version}</version>
        </dependency>
```

- 从Kafka消费数据

```java
        Properties properties = new Properties() {{
            this.setProperty("boostrap.servers", "172.37.4.155:9092");
            this.setProperty("group.id", "consumer-group");
        }};
        
        FlinkKafkaConsumer<ObjectNode> kafkaConsumer = new FlinkKafkaConsumer<>(
                "kafkaTopic",
                new JSONKeyValueDeserializationSchema(false), //要求Kafka中的数据已经序列化为比特数组
                properties
        );
        
        kafkaConsumer.setStartFromEarliest();     // 尽可能从最早的记录开始
        kafkaConsumer.setStartFromLatest();       // 从最新的记录开始
        kafkaConsumer.setStartFromTimestamp(1000); // 从指定的时间开始（毫秒）
        kafkaConsumer.setStartFromGroupOffsets(); // 默认的方法
        
        DataStream<ObjectNode> inputSource = env.addSource(kafkaConsumer);
```

Flink消费Kafka时支持分区偏移量**、**checkpoint容错**、**分区发现**、**时间戳抽取**以及**watermark 发送**，此处参考[官方文档](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/connectors/datastream/kafka/#kafka-consumers-start-position-configuration)。

## 自定义Source源

```java
    public static class WordCountSource implements SourceFunction<String> {

        public boolean flag = false;

        @Override
        public void run(SourceContext<String> ctx) throws Exception {
            List<String> sourceTemplate = new ArrayList<>() {{
                this.add("hello world");
                this.add("hello scala");
                this.add("hello flink");
                this.add("happy birthday");
                this.add("how about you");
                this.add("this is an unbounded stream");
            }};

            while (!flag) {
                for (String word : sourceTemplate) {
                    ctx.collect(word);
                }
                Thread.sleep(100);
            }
        }

        @Override
        public void cancel() {
            this.flag = true;
        }

    }
```



# Transform

|        Transform Type         |                   Function Meaning                   |                           Comment                            |
| :---------------------------: | :--------------------------------------------------: | :----------------------------------------------------------: |
|          MapFunction          |                 [□□□] → map → [●●●]                  |                       将数据一对一转换                       |
|        FlatMapFunction        |                [□] → flatMap → [●●●]                 |                       将数据一对多转换                       |
|        FilterFunction         |                [□□□] → filter → [□□]                 |                        将数据进行过滤                        |
|             KeyBy             |              [□□□] → keyBy → [{□},{□□}]              |    将数据进行分类并重分区 **(DataStream → KeyedStream)**     |
|      Rolling Aggregation      | [{□},{□□}] → sum\|min\|max\|minBy\|maxBy → [{□},{□}] | 将分组后的数据进行**滚动聚合** **(KeyedStream → DataStream)** |
|        ReduceFunction         |           [{□},{□□}] → reduce → [{●},{●}]            |  将分组后的数据进行**规约** **(KeyedStream → DataStream)**   |
| Split&Select (OutputSelector) |            [□□□] → split&select  → [□,□□]            | 将**数据流**拆分成多个组，可以理解为给数据流盖戳 **(DataStream → SplitedStream)** |
|         Connect&CoMap         |            [□,●●] → connect&coMap → [□●●]            | 将2个数据流合并到一个数据流 **(DataStreams → ConnectedStream)** |
|             Union             |              [□,□,□□] → union → [□□□□]               | 将多条数据类型相同的数据流合并成一条流 **(DataStreams → DataStream)** |

*补各种DataStream转换图*

# Sink

