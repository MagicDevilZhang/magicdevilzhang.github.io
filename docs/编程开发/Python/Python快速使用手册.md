---
layout: post
title: Python快速使用手册
permalink: /docs/编程开发/Python/Python快速使用手册
---

# 搭建Python项目

## 项目结构

```
    venv/
    apps/
        demo.py
        __init__.py
    main.py
```

## 主函数

```python
from apps.demo import print_hello

def main():
    print_hello()

if __name__ == '__main__':
    main()
```

其中`import`还可以用下列方式导入：

```python
import namespace.module.method as anothername
from namespace.module import {module1[, module2[, ... moduleN]] | *}
```

## 打包

*待补充...*

# 基本语法

## 算术与位运算符

> - 四则运算符： `+` `-` `*` `/`
> - 取模运算： `%`
> - 幂次运算：`**` ，例如 (2 ** 3 = 2^3 = 8)
> - 向下取整： `//` ，例如 (9 // 2 = 4)
> - 与或运算：`&` `|`
> - 异或运算：`^`
> - 取反运算：`~`
> - 移位运算：`>>` `<<`

## 赋值运算符

> - 简单赋值运算符： `=`
> - 算数赋值运算符：`+=` `-=` `*=` `/=` `**=` `//=`
> - 海象运算符（表达式内部赋值，Python3.8及以上）：`:=` ，例如 `if (n:=len(a)) > 20 : ...`

## 逻辑及成员运算符

> - 比较运算符：`==` `!=` `>` `<` `>=` `<=`
> - 逻辑运算符：`and` `or` `not`
> - 成员运算符：`in` `not in`
> - 身份运算符：`is` ，等价于 `id(obj1) == id(obj2)`

*[注] Python中一切皆对象，内置函数id()返回对象的唯一标识符（CPython为内存地址），标识符是一个整数。*

## 条件语句(if ... elif ... else ...)

```python
if 条件表达式[,条件表达式[,...[条件表达式]]]:
    函数体
[elif 条件表达式[,条件表达式[,...[条件表达式]]]:
    函数体]
[else 条件表达式[,条件表达式[,...[条件表达式]]]:
    函数体]
```

## 循环语句

- `while`循环条件

```python
while 条件表达式[,条件表达式[,...[条件表达式]]]:
    循环体
[else:
    跳出循环]
```

- `for`循环条件

```python
for 变量名[,变量名[,...变量名]] in 序列:
    循环体
[else:
    跳出循环]
```

# 函数与面向对象

## 函数及参数

```python
def 函数名([参数1[,参数2[,...[参数N]]]]):
    函数体
    [return [返回值]]
```

- **必选参数**：必需参数须以**正确的顺序**传入函数。调用时的数量必须和声明时的一样。

```python
def printme(str):
    print(str)

printme()
```

- **关键字参数**：关键字参数和函数调用关系紧密，函数调用使用**关键字参数来确定传入的参数值**。使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为Python解释器能够用参数名匹配参数值。

```python
def printinfo(name, age):
    print("名字: ", name)
    print("年龄: ", age)

printinfo(age=50, name="ryan")
```

- **默认参数**：调用函数时，如果没有传递参数，则会使用默认参数，默认参数必须放在**必选参数之后**。

```python
def printinfo(name, age=23):
    print("名字: ", name)
    print("年龄: ", age)

printinfo(name="ryan")
```

- **不定长参数**：一个函数能处理比当初声明时更多的参数。

加了星号`*`的参数会以`元组(tuple)`的形式导入，存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组。

```python
def demo_func(a, *r):
    print("{} is {}".format(a, r))

demo_func(20, 1, 2, 3, 4, 5)
```

加了两个星号`**`的参数会以`字典(dict)`的形式导入。

```python
def demo_func(username, **movie):
    for key, value in movie.items():
        print('{}喜欢{}: {}'.format(username, key, value))

demo_func('Ryan', movie=10, book=20, sport=15)
```

当需要**嵌入调用**不定长参数时，需要添加`**`做标记

```python
def print_a(**param):
    print(param)

def print_b(**param):
    print_a(**param)
```

## 闭包运算

值得注意的是，Python中方法可以被**引用传递**，因此可以容易实现闭包运算。

```python
def out_add(outer_val):
    def inner_add(inner_val):
        return inner_val + outer_val
    return inner_add

op = out_add(10)
print(op(30))
```

如果需要闭包内函数操作闭包外函数的变量，需要`nonlocal`关键字修饰。

```python
def func(count):
    def print_val(val):
        nonlocal count
        print("{}:{}".format((count := count + 1), val))
    return print_val

op = func(0)
op("a")
op("b")
op("c")
```

## lambda表达式

```python
# lambda 参数[,参数[,...,参数]]: 语句表达式
def out_add(outer_val):
    return lambda x: x + outer_val

op = out_add(10)
print(op(30))
```

## 面向对象

```python
class 子类名([父类1,[父类2,...[父类N]]]):
    ...
```

- **方法重写**：包括重写父类和类的专有方法等

> - `__init__` : 构造函数，在生成对象时调用
> - `__del__` : 析构函数，释放对象时使用
> - `__repr__ ` : 打印，转换
> - `__setitem__` : 按照索引赋值
> - `__len__` : 获得长度
> - `__cmp__` : 比较运算
> - `__call__` : 函数调用
> - `__add__` : 加运算
> - `__sub__` : 减运算
> - `__mul__` : 乘运算
> - `__truediv__` : 除运算
> - `__mod__` : 求余运算
> - `__pow__` : 乘方运算

例如构造函数，其子类是否需要调用父类构造方法可以分为如下情况：

> - 子类需要自动调用父类的方法：子类不重写`__init__()`方法，实例化子类后，会自动调用父类的__init__()的方法。
> - 子类不需要自动调用父类的方法：子类重写`__init__()`方法，实例化子类后，将不会自动调用父类的__init__()的方法。
> - 子类重写`__init__()`方法又需要调用父类的方法：使用super关键词：`super(子类名, self).__init__(**params)`

- 类属性与方法

> - `__private_attrs`: 私有属性，不能在类的外部被使用或直接访问。
> - `__private_method`: 私有方法，只能在类的内部调用。

# 数据结构

## 变量作用域原则 (LEGB原则)

> - Local(function): 函数内的变量名称
> - Enclosing function locals: 外部嵌套函数的变量名称
> - Global(module): 函数定义所在模块（文件）的变量名称
> - Builtin(Python): Python内置模块的变量名称

当需要调用外部全局变量时，可以在函数体内使用`global`关键字。

```python
tag = 100

def demo_func():
    global tag
    print("{}".format(tag))
```

可以用过内置函数`globals()`和`locals()`获取python的变量名和变量值，以`字典(dict)`形式返回。

*[注]for循环中的变量不是local的：但列表推导时，作用域是local的。*

```python
i = 100
for i in range(3):
    print(i)
    
# 输出为：0 1 2
```

## 不可变数据类型 (Number, String, Tuple)

*待补充...*

## 可变数据类型 (List, Dictionary, Set)

*待补充...*

## 迭代器与生成器

*待补充...*

# 内置函数

## 数据类型转换函数

*待补充...*

## 状态内置函数

- callable()
- eval()
- exec()
- compile()

## MapReduce类型函数

- filter()
- map()
- reduce()

# 参考链接

> - [Python文档](https://docs.python.org/3)
> - [Python标准库](https://docs.python.org/3/library/)
> - [Python菜鸟教程](https://www.runoob.com/python3/)
