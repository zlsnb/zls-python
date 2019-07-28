# 打印基本是能兼容很多类型 总之往里面扔就对了
# 打印一个变量类型和它的值
a = 1
print(type(a))
print(a)

# 打印字符串类型
print('hello world')

# 打印一个列表/元组 
# 区别：列表是可变的元组是不可变的 比如元组添加元素相当于又创建一个新的元组（看不懂别看了
# 一般用列表就好了 其实可以类比到数组嗯
# 一个列表可以是各种奇怪的东西
strange_list = [1, 'hahaha', 2.333]
more_stange_tuple = (555, '明天要上班了', ['不快乐' for i in range(100)])
print(strange_list)
print(more_stange_tuple)
