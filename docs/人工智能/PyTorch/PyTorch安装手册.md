---
layout: post
title: PyTorch安装手册
permalink: /docs/人工智能/PyTorch/PyTorch安装手册
---

# 安装配置Conda

PyTorch推荐安装在Conda环境下，以利于不同版本的维护。

- 下载Anaconda

```
https://www.anaconda.com/products/individual
```

- 配置Conda国内镜像源

可以在Anaconda Navigator的Channels中添加如下镜像源：

```
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
```

- 创建虚拟环境

若使用GUI界面，可在Environments中直接新建，推荐使用命令行，可以按如下步骤新建：

```
conda create -n conda-pytorch python=3.8
```

- 配置Pip3镜像源

在Conda中可以通过如下命令设置Pip3的镜像源

```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```



# 安装配置PyTorch及相关依赖库

- 在Anaconda中使用虚拟环境

```
conda activate conda-pytorch
```

- 安装依赖库

```
# 安装Jupyter Notebook
conda install jupyter notebook 
conda install Cython #pip3 install Cython

# 代码提示
pip3 install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
pip3 install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user

# 安装 PyTorch
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
```

- 设置Jupyter默认目录

修改`~/.jupyter/jupyter_notebook_config.py`文件

```
c.NotebookApp.notebook_dir = u'E:\\projects'
```

