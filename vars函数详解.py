'''
描述
vars() 函数返回对象object的属性和属性值的字典对象。
语法
vars() 函数语法：
vars([object])
参数
object -- 对象
返回值
返回对象object的属性和属性值的字典对象，如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()。
'''

print(vars())
#输出 {'__name__': '__main__', '__doc__': '\n描述\nvars() 函数返回对象object的属性和属性值的字典对象。\n语法\nvars() 函数语法：\nvars([object])\n参数\nob

class A:
    a=1
    __dict__ = 'ltf'
print(vars(A))
#输出 {'__module__': '__main__', 'a': 1, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}

a=A()
print(vars(a))
#输出 ltf

print(a.__dict__)
#输出 ltf