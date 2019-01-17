'''
描述
oct() 函数将一个整数转换成八进制字符串。
语法
oct 语法：
oct(x)
参数说明：
x -- 整数。
返回值
返回八进制字符串。
'''

print(oct(12))          #输出12的八进制 0o14
print(oct(-120))        #输出-12的二进制 -0o170
print(type(oct(12)))    #输出oct(12) 的类型 <class 'str'> 所以不能直接计算

print(int(oct(10),base=8)+int(oct(15),base=8))  #输出 25

#base 参数不可为空 为空默认参数为10进制 会报错 ValueError: invalid literal for int() with base 10: '0b1010'

#当然了，参数不仅可以接受十进制整数，八进制、十六进制也是可以的，只要是int型数据就合法。

print(oct(0b10010))    #输出0o22
print(oct(0o1357))     #输出0o1357
print(oct(0x2d9))      #输出0o1331