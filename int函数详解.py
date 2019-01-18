'''
int([x[,radix]])
如果参数是字符串，那么它可能包含符号和小数点。参数radix表示转换的基数（默认是10进制）。
它可以是[2,36]范围内的值，或者0。如果是0，系统将根据字符串内容来解析。
如果提供了参数radix，但参数x并不是一个字符串，将抛出TypeError异常；
否则，参数x必须是数值（普通整数，长整数，浮点数）。通过舍去小数点来转换浮点数。
如果超出了普通整数的表示范围，一个长整数被返回。
如果没有提供参数，函数返回0。

int(x, [base])
作用：
将一个数字或base类型的字符串转换成整数。
int(x=0)
int(x, base=10)，base缺省值为10，也就是说不指定base的值时，函数将x按十进制处理。
注：
1. x 可以是数字或字符串，但是base被赋值后 x 只能是字符串
2. x 作为字符串时必须是 base 类型，也就是说 x 变成数字时必须能用 base 进制表示
'''

#1.x是数字
print(int(2.1))     #输出 2
print(int(2e3))     #输出 2000
#print(int(1000,2))       #出错，base 被赋值后函数只接收字符串
#报错 TypeError: int() can't convert non-string with explicit base

#2.x是字符串
print(int('abc12',16))    #输出  703506
#print(int('tuifyg',16))   #出错  tuifyg  超过0-9 abcdef 超出16进制
#报错 ValueError: invalid literal for int() with base 16: 'tuifyg'

#3. base 可取值范围是 2~36，囊括了所有的英文字母(不区分大小写)，
# 十六进制中F表示15，那么G将在二十进制中表示16，依此类推....Z在三十六进制中表示35
#print(int('FZ',16))     # 出错，FZ不能用十六进制表示
#报错 ValueError: invalid literal for int() with base 16: 'FZ'
print(int('FZ',36))     #  575

#4.字符串 0x 可以出现在十六进制中，视作十六进制的符号，
# 同理 0b 可以出现在二进制中，除此之外视作数字 0 和字母 x
print(int('0x10', 16))  # 16，0x是十六进制的符号
#print(int('0x10', 17)) # 出错，'0x10'中的 x 被视作英文字母 x
print(int('0x10', 36))  # 42804，36进制包含字母 x


#参考博客  https://www.cnblogs.com/guyuyuan/p/6827987.html