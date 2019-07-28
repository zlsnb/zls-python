# 一般就是while和for循环
index = 1
while index < 10:
    print('hhh')
    index = index + 1

for i in range(10):
    print('hhh')

# range是一个很神奇的东西 一般是range(start, end, step) 大概就是首尾步长
for i in range(1, 10, 2):
    print(i)

# 还可以倒过来
for i in range(10, 1, -1):
    print(i)