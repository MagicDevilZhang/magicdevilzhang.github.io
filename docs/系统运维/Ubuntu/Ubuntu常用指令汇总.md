---
layout: post
title: Ubuntu常用开发环境安装
permalink: /docs/系统运维/Ubuntu/Ubuntu常用指令汇总
---

# 系统指令

- 将数据由内存同步到硬盘中： `sync`
- 关机指令： `shutdown now`
- 重启指令： `reboot now`
- 关闭系统： `halt`
- 进程详情： [`grep -ef | grep keyword`](https://www.runoob.com/linux/linux-comm-ps.html)
- 查看端口： `netstat -a | grep LISTEN`

# 程序管理指令

- apt列表更新： `apt-get update`
- apt程序更新： `apt-get upgrade`
- apt安装程序： `apt-get install software`

# 文件处理指令

- 转移路径： `cd path / ..`
- 当前路径： `pwd`
- 拷贝： `cp source target`
- 移动： `mv source target`
- 删除： `rm -f filepath`
- 查找： `find path -type FileType -name '*.*' `
- 创建目录： `mkdir -p name`
- 查看当前目录：`ll -rt` 其中`-r`是倒置，`-t`按时间排序

# 权限指令

# 命令行

- 复制粘贴： `Ctrl + Shift + C` 以及 `Ctrl + Shift + V`
- 历史命令： `histroy | grep keyword`

# 远程操作

- 远程连接： `ssh username@hostname`
- 远程移动： `scp source hostname:target`

# 程序操作

- 后台运行： `nohup ./bin/launcher run &`

# 压缩与解压

- Tar解压： [`tar -zxvf tarpath`](https://www.runoob.com/linux/linux-comm-tar.html)
- Tar压缩： [`tar -zcvf targetname sourcefile`](https://www.runoob.com/linux/linux-comm-tar.html)

# 文档编辑

- 查看文档： `cat filename | grep keyword`
- 编辑文档： `vim filename`
  - 编辑模式： `a`
  - 强制退出： `:q!`
  - 保存退出： `:wq`
  - 撤销操作： `u`
  - 查找： `:/keyword`
  - 跳转到某行： `:line`
  - 翻页： `ctrl` + `f`(forward) / `b`(backward)
- 翻页： `Shift + PageUp` 以及 `Shift + PageDown`
