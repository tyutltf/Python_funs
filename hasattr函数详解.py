'''
hasattr()函数用于判断是否包含对应的属性
语法：
hasattr(object,name)
参数：
object--对象
name--字符串，属性名
返回值：
如果对象有该属性返回True，否则返回False
'''

class People():
    sex='男'
    def __init__(self,name):
        self.name=name
    def peopleinfo(self):
        print('欢迎%s访问'%self.name)

obj=People('zhangsan')
print(hasattr(People,'sex'))    #输出 True
print('sex'in People.__dict__)  #输出 True

print(hasattr(obj,'peopleinfo'))  #输出 True
print(People.__dict__)
#输出 {'__module__': '__main__', 'sex': '男', '__init__': <function People.__init__ at 0x0000019931C452F0>, 'peopleinfo': <function People.peopleinfo at 0x0000019931C45378>, '__dict__': <attribute '__dict__' of 'People' objects>, '__weakref__': <attribute '__weakref__' of 'People' objects>, '__doc__': None}