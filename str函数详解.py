'''
描述
str() 函数将对象转化为适于人阅读的形式。
语法
以下是 str() 方法的语法:
class str(object='')
参数
object -- 对象。
返回值
返回一个对象的string格式。
'''

print(str(1))             #输出  字符串1
print(type(str(1)))       #输出  <class 'str'>
print(str(b'\xe5\xbc\xa0\xe4\xb8\x89',encoding='utf-8'))  #输出张三

dict={'zhangsan':'zhang1234','lisi':'li1234'}
print(type(dict))         #输出  <class 'dict'>
a=str(dict)
print(str(dict))          #输出  字符串 {'zhangsan': 'zhang1234', 'lisi': 'li1234'}
print(type(a))            #输出  <class 'str'>