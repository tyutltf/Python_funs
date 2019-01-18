'''
描述：
getattr()函数用于返回一个对象属性值
语法：
getattr(object,name,default)
参数：
object--对象
name--字符串，对象属性
default--默认返回值，如果不提供该参数，在没有对应属性时，将触发AttributeError。
返回值：
返回对象属性值
'''

class People():
    sex='男'
    def __init__(self,name):
        self.name=name
    def peopleinfo(self):
        print('欢迎%s访问'%self.name)

obj=getattr(People,'sex')
print(obj)       #返回值  男

#obj=getattr(People,'sexage')
#print(obj)
'''
报错。。。
Traceback (most recent call last):
  File "G:/pythonAI/Python_funs/getattr函数详解.py", line 24, in <module>
    obj=getattr(People,'sexage')
AttributeError: type object 'People' has no attribute 'sexage'
'''

obj=getattr(People,'sexage',None)
print(obj)    #返回值 None