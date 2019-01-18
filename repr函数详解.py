'''
描述
repr() 函数将对象转化为供解释器读取的形式。
语法
以下是 repr() 方法的语法:
repr(object)
参数
object -- 对象。
返回值
返回一个对象的 string 格式。
'''

s='qwerasdf'
print(s)            #输出  qwerasdf
print(repr(s))      #输出  'qwerasdf'

dict={'a':1,'b':2}
print(dict)         #输出 {'a': 1, 'b': 2}
print(repr(dict))   #输出 {'a': 1, 'b': 2}  没改变么

print(repr([0,1,2,3,4]))         #输出 [0, 1, 2, 3, 4]
print(repr('hello'))             #输出 'hello'

print(str(1.0/7.0))              #输出 0.14285714285714285
print(repr(1.0/7.0))             #输出 0.14285714285714285