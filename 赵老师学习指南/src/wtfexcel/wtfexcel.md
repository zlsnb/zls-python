# 用Python操作Excel

# 可以用的库

## openpyxl

可以读写.xlsx（墙裂推荐

## xlsxwriter

也是读写.xlsx的

## xlrd xlwt xlutils

仅限于老表（.xls)的读写等操作，先不管了 /手动挥手

# 写之前要干什么

安装一下python，具体请移步[环境安装][python_env_install]

[python_env_install]: /赵老师学习指南/环境安装.md

然后就使用pip安装一下openpyxl叭

```
pip3 install openpyxl
```

安装完后在terminal应该能看到这么一句话（这是我的terminal）
```
You are using pip version 18.1, however version 19.2.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```
然后就可以愉快的开始写了w

# 这都什么玩意儿

一般会涉及到的类

|  相关类  |            瞎**解释           |
|:--------:|:-----------------------------:|
| Workbook | 可以理解为这就是一个excel文档 |
|   sheet  |     一个excel里面的一张表     |
|   cell  |     一个cell代表一个单元格     |


# 让我看看(这两个字被屏蔽了)网友都写了什么(然后又被屏蔽了)

[excel读写等基本操作][baseop_excel]

[合并两个excel表][merge_excel]

[baseop_excel]: baseop_excel.py

[merge_excel]: merge_excel.py

# 快去深入学习一下
[openpyxl官网][openpyxl]

[openpyxl]: https://openpyxl.readthedocs.io/en/stable/