'''
描述：
delattr函数用于删除属性
delattr(x,'foobar)相当于del x.foobar
语法：
setattr(object,name)
参数：
object--对象
name--必须是对象的属性
返回值：
无
'''

class People():
    sex='男'
    def __init__(self,name):
        self.name=name
    def peopleinfo(self):
        print('欢迎%s访问'%self.name)

delattr(People,'sex')  #等同于 del People.sex
print(People.__dict__)

#输出 {'__module__': '__main__', '__init__': <function People.__init__ at 0x000001CE3E2E52F0>, 'peopleinfo': <function People.peopleinfo at 0x000001CE3E2E5378>, '__dict__': <attribute '__dict__' of 'People' objects>, '__weakref__': <attribute '__weakref__' of 'People' objects>, '__doc__': None}

class Foo:
    def run(self):
        while True:
            cmd=input('cmd>>: ').strip()
            if hasattr(self,cmd):
                func=getattr(self,cmd)
                func()
    def download(self):
        print('download....')
    def upload(self):
        print('upload...')
obj=Foo()
obj.run()