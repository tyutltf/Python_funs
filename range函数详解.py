'''
python range() 函数可创建一个整数列表，一般用在 for 循环中。
函数语法
range(start, stop[, step])
参数说明：
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

'''

for i in range(10):
    print(i)  #输出 从0-9

for i in range(0,11,2):
    print(i)  #输出 0,2,4,6,8,10

for i in range(0,-10,-3):
    print(i)  #输出 0,-3,-6,-9

list=[]
for i in range(5,-5,-1):
    list.append(i)
print(list)   #输出 [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]

for i in 'ahfgohiauf':
    print(i)   #依次输出字符

#参考博客 https://www.cnblogs.com/101718qiong/p/7542193.html

