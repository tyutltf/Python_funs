'''
python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
在 python 2.3 版本之前不允许处理复数。
函数语法
divmod(a, b)
参数说明：
a: 数字
b: 数字
'''
print(divmod(20,4))   #返回  (5, 0)
print(divmod(7,2))    #返回  (3, 1)
print(divmod(8,2))    #返回  (4, 0)
#print(divmod(1+2j,1+0.5j))
#报错 TypeError: can't take floor or mod of complex number.