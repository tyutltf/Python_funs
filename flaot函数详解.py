'''
描述
float() 函数用于将整数和字符串转换成浮点数。
语法
float()方法语法：
class float([x])
参数
x -- 整数或字符串
返回值
返回浮点数。
'''
print(float(1))            #输出  1.0
print(float(112.0))        #输出  112.0
print(float('123'))        #输出  123.0
print(float(True))         #输出  1.0
print(float(False))        #输出  0.0

#print(float('a'))
#报错 ValueError: could not convert string to float: 'a'

#可以参考博客 https://blog.csdn.net/TCatTime/article/details/82932818