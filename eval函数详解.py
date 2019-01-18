'''
eval() 函数用来执行一个字符串表达式，并返回表达式的值。
语法
以下是 eval() 方法的语法:
eval(expression[, globals[, locals]])
参数
expression -- 表达式。
globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
返回值
返回表达式计算结果。
'''
x=7
print(eval('3*x'))        #返回 21
print(eval('pow(2,2)'))   #返回 4
print(eval('3+5'))        #返回 8


#eval函数还可以实现list、dict、tuple与str之间的转化

#1.字符串转换成列表
a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
print(type(a))         #返回  <class 'str'>
b = eval(a)
print(type(b))         #返回  <class 'list'>
print(b)               #输出  [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]

#2.字符串转换成字典
a = "{1: 'a', 2: 'b'}"
print(type(a))        #返回  <class 'str'>
b = eval(a)
print(type(b))        #返回  <class 'dict'>
print(b)              #输出  {1: 'a', 2: 'b'}

#3.字符串转换成元组
a = "([1,2], [3,4], [5,6], [7,8], (9,0))"
print(type(a))        #返回 <class 'str'>
b=eval(a)
print(type(b))        #返回 <class 'tuple'>
print(b)              #输出 ([1, 2], [3, 4], [5, 6], [7, 8], (9, 0))