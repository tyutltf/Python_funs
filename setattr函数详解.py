'''
描述：
setattr函数，用于设置属性值，该属性必须存在
语法：
setattr(object,name,value)
参数：
object--对象
name--字符串，对象属性
value--属性值
返回值：
无
'''

class People():
    sex='男'
    def __init__(self,name):
        self.name=name
    def peopleinfo(self):
        print('欢迎%s访问'%self.name)

obj=People('zhangsan')
setattr(People,'x',123)
print(People.x)  #等同于 Peopel.x=123

setattr(obj,'age',18)
print(obj.__dict__)   #输出 {'name': 'zhangsan', 'age': 18}

print(People.__dict__)
#输出
#{'__module__': '__main__', 'sex': '男', '__init__': <function People.__init__ at 0x00000259A92752F0>, 'peopleinfo': <function People.peopleinfo at 0x00000259A9275378>, '__dict__': <attribute '__dict__' of 'People' objects>, '__weakref__': <attribute '__weakref__' of 'People' objects>, '__doc__': None, 'x': 123}