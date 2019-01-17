'''
challable()　　判断对象是否可以被调用，
能被调用的对象就是一个callables对象，
比如函数和带有__call__()的实例
'''

print(callable(max))       #输出True
print(callable([1,2,3]))   #输出Fasle
print(callable(None))      #输出Fasle
print(callable('str'))     #输出Fasle


def fn(x):
    return x*x
print(callable(fn))        #输出True  证明自定义的函数也可以