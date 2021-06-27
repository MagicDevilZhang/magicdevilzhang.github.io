---
layout: post
title: Ubuntu常用开发环境安装
permalink: /docs/系统运维/Ubuntu/Ubuntu常用开发环境安装
---

# 安装JDK8

```
sudo apt-get install openjdk-8-jdk
sudo vim ~/.bashrc
```

```
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export CLASSPATH=.:$CLASSPATH:$JAVA_HOME/lib:$JAVA_HOME/jre/lib
export PATH=$PATH:$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH:$HOME/bin
```

```
source ~/.bashrc
sudo update-alternatives --config  java     #选择Java默认版本
```

# 安装Python

```
sudo apt install python
sudo apt install python3
sudo update-alternatives --config python    #选择Python默认版本
```
