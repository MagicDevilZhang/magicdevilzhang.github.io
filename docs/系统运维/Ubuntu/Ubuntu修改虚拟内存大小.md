---
layout: post
title: Ubuntu修改虚拟内存大小
permalink: /docs/系统运维/Ubuntu/Ubuntu修改虚拟内存大小
---

- 查看内存大小

```
free -m  
```

- 卸载当前虚拟内存交换文件

```
sudo swapoff /swapfile
```

- 设置虚拟内存大小

```
sudo dd if=/dev/zero of=/swapfile bs=1M count=4096
```

- 修改权限

```
sudo chmod 600 /swapfile
```

- 格式化

```
sudo mkswap /swapfile
```

- 开启虚拟内存

```
sudo swapon /swapfile
```

- 设置配置文件

```
sudo vim /etc/fstab
```

```
/swapfile swap swap defaults 0 0
```

- 查看设置好的虚拟内存

```
sudo swapon -s
sudo free -m
```