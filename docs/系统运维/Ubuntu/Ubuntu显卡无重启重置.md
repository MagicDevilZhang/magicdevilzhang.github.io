---
layout: post
title: Ubuntu显卡无重启重置
permalink: /docs/系统运维/Ubuntu/Ubuntu显卡无重启重置
---

# Ubuntu显卡无重启重置

```shell
systemctl isolate multi-user.target  # 关闭可视化界面
sudo rmmod nvidia_drm  # 停用显卡驱动
sudo modprobe nvidia_drm  # 启用显卡驱动
systemctl start graphical.target  # 启动可视化界面
```

