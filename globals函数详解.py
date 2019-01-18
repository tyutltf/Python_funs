'''
描述
globals() 函数会以字典类型返回当前位置的全部全局变量。
语法
globals() 函数语法：
globals()
参数
无
返回值
返回全局变量的字典
'''
a='ltftyut1234'
print(globals()) # globals 函数返回一个全局变量的字典，包括所有导入的变量。
#  {'__name__': '__main__', '__doc__': '\n描述\nglobals() 函数会以字典类型返回当前位置的全部全局变量。\n语法\nglobals() 函数语法：\nglobals()\n参数\n无\n返回值\n返回全局变量的字典\n', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001C5A50FB4E0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'G:/pythonAI/Python_funs/globals函数详解.py', '__cached__': None, 'a': 'ltftyut1234'}



def zero_promo():
    return 0

def one_promo():
    return 1

def two_promo():
    return 2

def hello():
    print("Hello")

if __name__ == '__main__':
    promos = [name for name in globals()if name.endswith("_promo")]
    print(promos)   #输出 ['zero_promo', 'one_promo', 'two_promo']

    promos = [globals()[name] for name in globals() if name.endswith("_promo")]
    print(promos[0]())    #输出 0  调用了第一个函数

#参考博客  https://www.jianshu.com/p/a9f583d8cbaa

