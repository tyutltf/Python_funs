'''
描述
next() 返回迭代器的下一个项目。
语法
next 语法：
next(iterator[, default])
参数说明：
iterator -- 可迭代对象
default -- 可选，用于设置在没有下一个元素时返回该默认值，如果不设置，又没有下一个元素则会触发 StopIteration 异常。
返回值
返回对象帮助信息。
'''

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

a=iter('abcde')
print(next(a))    #输出 a
print(next(a))    #输出 b
print(next(a))    #输出 c
print(next(a))    #输出 d
print(next(a))    #输出 e
#print(next(a))    #报错 StopIteration

#函数可以接收一个可选的default参数，传入default参数后，
# 如果可迭代对象还有元素没有返回，则依次返回其元素值，如果所有元素已经返回，
# 则返回default指定的默认值而不抛出StopIteration 异常。

print(next(a,'e'))   #这次不报错了 返回 e 即default参数

#参考博客  http://www.cnblogs.com/sesshoumaru/p/6037922.html
