'''
abs() 函数返回数字的绝对值。
绝对值：absolute
正如字面上的意思，可以返回一个绝对值
'''
import math
print('abs(45)的值:',abs(45))
print('abs(-45)的值:',abs(-45))
print('abs(45+23)的值:',abs(45+23))
print('abs(math.pi)的值:',abs(math.pi))

print(help(abs))
'''
运行结果：
abs(45)的值: 45
abs(-45)的值: 45
abs(45+23)的值: 68
abs(math.pi)的值: 3.141592653589793
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

None

在python2 里还可以输出 print "abs(119L) : ", abs(119L)  不过python3中abs函数只能输入int型 不然会报错
'''
