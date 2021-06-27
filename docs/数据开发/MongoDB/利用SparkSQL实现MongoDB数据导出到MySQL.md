---
layout: post
title: 利用SparkSQL实现MongoDB数据导出到MySQL
permalink: /docs/数据开发/MongoDB/利用SparkSQL实现MongoDB数据导出到MySQL
---

```sql
select
  tmp._id,
  tmp.name, 
  tmp.age,
  tmp.element.sid,
  tmp.element.name,
  tmp.element.year
from 
  ( select _id, name, age, explode(testCollection.study) as element
    from testCollection ) as tmp
```

```
package com.yunzhangfang.di.spark.test;

import com.mongodb.spark.MongoSpark;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

import java.io.Serializable;
import java.util.Properties;

public class MongoDBToSpark implements Serializable {

    public static void main(String[] args) throws Exception {
        //启动Spark
        SparkSession spark = SparkSession.builder()
                .master("local[3]")
                .appName("MongoDBToSpark")
                .config("spark.mongodb.input.uri", "mongodb://crm:crm1883@172.24.189.3:27017/enterprise_crm.biz_opportunity_new")
                .getOrCreate();

        //从MongoDB中将数据读到source中
        Dataset<Row> source = MongoSpark
                .load(JavaSparkContext.fromSparkContext(spark.sparkContext()))
                .toDF();

        //输出MongoDB数据结构
        source.printSchema();

        //将MongoDB数据在Spark SQL中创建映射表
        source.createTempView("biz_opportunity_new");

        //执行SQL开窗函数
        /**
         * MongoDB中`clue_assign_task_log`的表结构如下
         * clue_assign_task_log
         *  |-- _class: string (nullable = true)
         *  |-- _id: struct (nullable = true)
         *  |    |-- oid: string (nullable = true)
         *  |-- assign_clues: array (nullable = true)
         *  |    |-- element: struct (containsNull = true)
         *  |    |    |-- assign_status: integer (nullable = true)
         *  |    |    |-- clue_id: string (nullable = true)
         *  |    |    |-- cust_name: string (nullable = true)
         *  |    |    |-- fail_reason: string (nullable = true)
         *  |-- assign_task_id: string (nullable = true)
         *  |-- end_time: timestamp (nullable = true)
         *  |-- operator_id: string (nullable = true)
         *  |-- start_time: timestamp (nullable = true)
         *  |-- status: integer (nullable = true)
         *
         * 将嵌套的内联属性用过开窗函数映射到一张表上
         *  select
         *     info_template._id.oid as id,
         *     info_template.assign_task_id as assign_task_id,
         *     info_template.operator_id as operator_id,
         *     info_template.start_time as start_time,
         *     info_template.end_time as end_time,
         *     info_template.status as status,
         *     info_1.assign_clues.clue_id as assign_clues_id,
         *     info_1.assign_clues.cust_name as assign_clues_name,
         *     info_1.assign_clues.assign_status as assign_status,
         *     info_1.assign_clues.fail_reason as assign_fail_reason
         *   from
         *     clue_assign_task_log as info_template
         *     join
         *     ( select _id.oid as id, explode(assign_clues) as assign_clues
         *       from clue_assign_task_log ) as info_1
         *     on info_template._id.oid = info_1.id
         *
         */
        Dataset<Row> result = spark.sql(
                " select  " +
                        "   info_template._id.oid as id, " +
                        "   info_template.assign_task_id as assign_task_id, " +
                        "   info_template.operator_id as operator_id, " +
                        "   info_template.start_time as start_time, " +
                        "   info_template.end_time as end_time, " +
                        "   info_template.status as status, " +
                        "   info_1.assign_clues.clue_id as assign_clues_id, " +
                        "   info_1.assign_clues.cust_name as assign_clues_name, " +
                        "   info_1.assign_clues.assign_status as assign_status, " +
                        "   info_1.assign_clues.fail_reason as assign_fail_reason " +
                        " from " +
                        "    clue_assign_task_log as info_template " +
                        "    join " +
                        "    ( select _id.oid as id, explode(assign_clues) as assign_clues " +
                        "      from clue_assign_task_log ) as info_1 " +
                        "    on info_template._id.oid = info_1.id ");


        //将数据写入到MySQL
        Properties connectionProperties = new Properties();
        {
            connectionProperties.put("driver", "com.mysql.jdbc.Driver");
            connectionProperties.put("user", "root");
            connectionProperties.put("password", "mysqladmin");
        }

        result.write().jdbc("jdbc:mysql://172.37.4.155:3306/sale_ods?useUnicode=true&characterEncoding=utf8"
                , "clue_assign_task_log", connectionProperties);

//        result.show(10);
//        result.write()
//                .format("com.crealytics.spark.excel")
//                .option("header", "true")
//                .save("/home/yzf/clue_assign_task_log.xlsx");

        //退出关闭Spark
        spark.close();
    }
}

```