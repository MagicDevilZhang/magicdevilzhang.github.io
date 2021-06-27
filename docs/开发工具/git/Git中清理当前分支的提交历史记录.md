---
layout: post
title: Git中清理当前分支的提交历史记录
permalink: /docs/开发工具/git/Git中清理当前分支的提交历史记录
---

**若当前分支是`dev`，清楚所有提交记录可以采用如下方案：**

- 在当前分支的基础上建立一个没有任何提交记录的新分支

`--orphan`会基于当前所在分支新建一个赤裸裸的分支，没有任何的提交历史，但是当前分支的内容俱全。

```
git checkout --orphan latest_branch
```

- 添加所有文件

```
git add -A
```

- 提交更改

```
git commit -am "merge commits"
```

- 删除原分支

```
git branch -D dev
```

- 将当前分支重命名为原分支

```
git branch -m dev
```

- 强制更新存储库

```
git push -f origin dev
```