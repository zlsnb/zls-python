# 特别简单的使用Python P图

# Pillow

一个挺好用的图像处理库

接着在Python3下安装

```
pip3 install  Pillow
```

目前主要用到的是**Image**这个类（我只会这个

需要注意的就是
```
box = [x, y, x + img_sub.size[0], y + img_sub.size[1]]
```
这里界定了一个矩形区域来放子图
（示例后面再更
