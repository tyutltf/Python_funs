'''
locals() 函数会以字典类型返回当前位置的全部局部变量。
对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
语法
locals() 函数语法：
locals()
参数
无
返回值
返回字典类型的局部变量

1 不要修改locals()返回的字典中的内容；改变可能不会影响解析器对局部变量的使用。
2 在函数体内调用locals()，返回的是自由变量。修改自由变量不会影响解析器对变量的使用。
3 不能在类区域内返回自由变量。
'''

def test_py(arg):
    z=1
    print(locals())
test_py(6)   #输出 {'z': 1, 'arg': 6}


def foo(arg, a):
    x = 100
    y = 'hello python!'
    for i in range(10):
        j = 1
        k = i
    print(locals())
foo(1, 2)   #输出 {'k': 9, 'j': 1, 'i': 9, 'y': 'hello python!', 'x': 100, 'a': 2, 'arg': 1}

#参考博客 https://blog.csdn.net/sxingming/article/details/52061630


