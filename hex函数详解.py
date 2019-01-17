'''
描述
hex() 函数将一个整数转换成十六进制字符串。
语法
hex 语法：
hex(x)
参数说明：
x -- 整数。
返回值
返回十六进制字符串。
'''
print(hex(12))          #输出12的八进制 0xc
print(hex(-120))        #输出-12的二进制 -0x78
print(type(hex(12)))    #输出oct(12) 的类型 <class 'str'> 所以不能直接计算

print(int(hex(10),base=16)+int(hex(15),base=16))  #输出 25

#base 参数不可为空 为空默认参数为10进制 会报错 ValueError: invalid literal for int() with base 10: '0b1010'

#当然了，参数不仅可以接受十进制整数，八进制、十六进制也是可以的，只要是int型数据就合法。

print(hex(0b10010))    #输出0x12
print(hex(0o1357))     #输出0x2ef
print(hex(0x2d9))      #输出0x2d9