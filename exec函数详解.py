'''
函数的作用：
动态执行python代码。也就是说exec可以执行复杂的python代码，而不像eval函数那样只能计算一个表达式的值。
exec(source, globals=None, locals=None, /)
source：必选参数，表示需要被指定的python代码。它必须是字符串或code对象。如果source是一个字符串，该字符串会先被解析为一组python语句，然后执行。如果source是一个code对象，那么它只是被简单的执行。
返回值：
exec函数的返回值永远为None。

eval()函数和exec()函数的区别：
eval()函数只能计算单个表达式的值，而exec()函数可以动态运行代码段。
eval()函数可以有返回值，而exec()函数返回值永远为None。
'''

x = 10
def func():
    y = 20
    a = exec("x+y")
    print("a:",a)         #输出  a: None
    b = exec("x+y",{"x":1,"y":2})
    print("b:",b)         #输出  b: None
    c = exec("x+y",{"x":1,"y":2},{"y":3,"z":4})
    print("c:",c)         #输出  c: None
    d = exec("print(x,y)")
    print("d:",d)         #输出  d: None
func()



x = 10
expr = """
z = 30
sum = x + y + z   #一大包代码
print(sum)
"""
def func():
    y = 20
    exec(expr)   #10+20+30       输出60
    exec(expr,{'x':1,'y':2}) #30+1+2         输出 33
    exec(expr,{'x':1,'y':2},{'y':3,'z':4}) #30+1+3，x是定义全局变量1，y是局部变量  输出34

func()

#参考原博客 https://www.cnblogs.com/yangmingxianshen/p/7810496.html