'''
函数原型
bin(x)
参数解释
x
整数型，参数不可为空。
返回值
<class 'str'> 字符串类型，二进制整数。
函数说明
将一个整数转化为一个二进制整数，并以字符串的类型返回。
'''
print(bin(12))          #输出12的二进制 0b1100
print(bin(-120))        #输出-12的二进制 -0b1111000
print(type(bin(12)))    #输出bin(12) 的类型 <class 'str'> 所以不能直接计算

print(int(bin(10),base=2)+int(bin(20),base=2))  #输出 30

#base 参数不可为空 为空默认参数为10进制 会报错 ValueError: invalid literal for int() with base 10: '0b1010'

#当然了，参数不仅可以接受十进制整数，八进制、十六进制也是可以的，只要是int型数据就合法。

print(bin(0b10010))    #输出0b10010
print(bin(0o1357))     #输出0b1011101111
print(bin(0x2d9))      #输出0b1011011001