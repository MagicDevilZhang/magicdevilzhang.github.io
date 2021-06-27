---
layout: post
title: Matplotlib组件使用
permalink: /docs/编程开发/Python/Matplotlib组件使用
---

# 安装Matplotlib

```
python -m pip install matplotlib
```

# 核心方法

> - 生成画图板：[plt.figure()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)
> - 设置X轴的含义：[plt.xlabel()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html)
> - 设置X轴刻度：[plt.xticks()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html)
> - 添加折线：[plt.plot()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
> - 添加散点：[plt.scatter()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)
> - 添加柱状图：[plt.bar()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)
> - 保存统计图：[plt.savefig()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)
> - 显示统计图：[plt.show()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)

# 常用例图

## 折线图

- 核心方法：[plt.plot()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)

```python
from random import randint
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm

# 产生数据
x = [v for v in range(1, 100, 5)]
y_1 = [randint(40, 100) for v in range(1, 100, 5)]
y_2 = [randint(20, 80) for v in range(1, 100, 5)]

# 配置图的尺寸
plt.figure(figsize = (20, 8), dpi = 300)

# 配置中文等字体显示
my_font = fm.FontProperties(fname = r"C:\Windows\Fonts\simsun.ttc", size = 12)

# 将坐标轴刻度集合进行投影到字符串集合
xticks_label = [v for v in range(1, 100, 5)]
yticks_label = [v for v in range(0, 101, 10)]
xticks_label_format = ["{}岁".format(v) for v in range(1, 100, 5)]
yticks_label_format = ["{}%".format(v) for v in range(0, 101, 10)]

#设置坐标轴含义
plt.xlabel("年龄(单位:岁)", fontproperties = my_font)
plt.ylabel("含量(单位:比率)", fontproperties = my_font)

#设置坐标轴刻度显示格式
plt.xticks(xticks_label, xticks_label_format, fontproperties = my_font, rotation = 45)
plt.yticks(yticks_label, yticks_label_format, fontproperties = my_font)

# 设置图的标题
plt.title("各年龄段男性与女性体内某种元素的含量", fontproperties = my_font)

# 将数据插入到图中
plt.plot(x, y_1, label = "男性", linewidth = 5, color = "blue", alpha = 0.3, linestyle = "--")
plt.plot(x, y_2, label = "女性", linewidth = 5, color = "red", alpha = 0.3, linestyle = ":")
plt.legend(loc = "upper left", prop = my_font)

# 图保存并显示
plt.savefig("./analysis.png")
plt.show()
```

## 散点图

- 核心方法：[plt.scatter()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)

```python
from random import randint, uniform
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm

# 产生数据
x_1 = [ t for t in range(1, 31) ]
y_1 = [ uniform(15.0,30.0) for v in range(30) ]
x_2 = [ t for t in range(1, 31) ]
y_2 = [ uniform(0.0,20.0) for v in range(30) ]

x = [1, 30]
y = [8, 23]

# 配置图的尺寸
plt.figure(figsize = (15, 3), dpi = 300)

# 配置中文等字体显示
my_font = fm.FontProperties(fname = r"C:\Windows\Fonts\simsun.ttc", size = 12)

# 将坐标轴刻度集合进行投影到字符串集合
xticks_label = [v for v in range(1, 31)]
yticks_label = [v for v in range(0, 41, 5)]
xticks_label_format = ["{}天".format(v) for v in range(1, 31)]
yticks_label_format = ["{}℃".format(v) for v in range(0, 41, 5)]

#设置坐标轴含义
plt.xlabel("日期(单位:天)", fontproperties = my_font)
plt.ylabel("气温(单位:℃)", fontproperties = my_font)

#设置坐标轴刻度显示格式
plt.xticks(xticks_label, xticks_label_format, fontproperties = my_font, rotation = 45)
plt.yticks(yticks_label, yticks_label_format, fontproperties = my_font)

# 设置图的标题
plt.title("某城市某月气温统计图", fontproperties = my_font)

# 将数据插入到图中
plt.plot(x, y, color = "blue", alpha = 0.6, linewidth = 2, linestyle = ":")
plt.scatter(x_1, y_1, label = "A城市", color = "green", alpha = 0.6, marker = "+")
plt.scatter(x_2, y_2, label = "B城市", color = "red", alpha = 0.6, marker = "+")
plt.legend(loc = "upper left", prop = my_font)

# 图保存并显示
plt.savefig("./analysis.png")
plt.grid(alpha = 0.3)
plt.show()
```

## 条形图

- 核心方法：

> - [bar()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)
> - [barh()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html)

```python
from random import randint, uniform
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm

# 产生数据
x = [ v for v in range(10) ]
y = [randint(5,40) for v in range(10) ]

# 配置图
plt.figure(figsize = (20, 12), dpi = 300)

# 配置中文等字体显示
my_font = fm.FontProperties(fname = r"C:\Windows\Fonts\simsun.ttc", size = 12)

# 将坐标轴刻度集合进行投影到字符串集合
xticks_label = [v for v in range(10)]
yticks_label = [v for v in range(0, 50, 2)]
xticks_label_format = [chr(ord('A')+v)+"城市" for v in range(10)]
yticks_label_format = ["{}℃".format(v) for v in range(0, 50, 2)]

#设置坐标轴含义
plt.xlabel("城市", fontproperties = my_font)
plt.ylabel("气温(单位:℃)", fontproperties = my_font)

#设置坐标轴刻度显示格式
plt.xticks(xticks_label, xticks_label_format, fontproperties = my_font, rotation = 45)
plt.yticks(yticks_label, yticks_label_format, fontproperties = my_font)

# 设置图的标题
plt.title("城市某月气温统计图", fontproperties = my_font)

# 将数据插入到图中
plt.bar(x, y, width = 0.8, color = "green", hatch = '/', alpha=0.8)

# 图保存并显示
plt.savefig("./analysis.png")
plt.grid(alpha = 0.3)
plt.show()
```

# 参考链接

> - [Matplotlib官方网站](https://matplotlib.org/)
> - [Matplotlib官方样例](https://matplotlib.org/stable/gallery/index.html)