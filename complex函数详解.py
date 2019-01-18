'''
描述
complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。
如果第一个参数为字符串，则不需要指定第二个参数。。
语法
complex 语法：
class complex([real[, imag]])
参数说明：
real -- int, long, float或字符串；
imag -- int, long, float；
返回值
返回一个复数。
'''

print(complex(1,2))          #输出  (1+2j)
print(complex(1))            #输出  (1+0j)
print(complex('2'))          #输出  (2+0j)

# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
print(complex('2+3j'))       #输出  (2+3j)

print(complex(1.2,3.4))      #输出  (1.2+3.4j)