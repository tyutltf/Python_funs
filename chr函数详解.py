'''
查看十进制数对应的ASCII码值
描述
chr() 用一个整数作参数，返回一个对应的字符。
语法
以下是 chr() 方法的语法:
chr(i)
参数
i -- 可以是 10 进制也可以是 16 进制的形式的数字，数字范围为 0 到 1,114,111 (16 进制为0x10FFFF)。
返回值
返回值是当前整数对应的 ASCII 字符。
'''

#print(chr(-1))   #报错 ValueError: chr() arg not in range(0x110000) 超出范围 不能小于0

print(chr(0x30))     #输出 0
print(chr(97))       #输出 a
print(chr(8364))     #输出 €
