'''
匿名函数lambda：是指一类无需定义标识符（函数名）的函数或子程序。
lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值。

要点：
1，lambda 函数不能包含命令，

2，包含的表达式不能超过一个。

说明：一定非要使用lambda函数；任何能够使用它们的地方，都可以定义一个单独的普通函数来进行替换。
我将它们用在需要封装特殊的、非重用代码上，避免令我的代码充斥着大量单行函数。

lambda匿名函数的格式：冒号前是参数，可以有多个，用逗号隔开，冒号右边的为表达式。
其实lambda返回值是一个函数的地址，也就是函数对象。
'''
def sum(x,y):
    return x+y
print(sum(4,6))

f=lambda x,y:x+y
print(f(4,6))
#这俩个例子的效果是一样的，都是返回x+y

a=lambda x:x*x
print(a(4))  #传入一个参数的lambda函数 返回x*x

b=lambda x,y,z:x+y*z
print(b(1,2,3))  #返回x+y*z  即1+2*3=7

#2.方法结合使用
from functools import reduce
foo=[2, 18, 9, 22, 17, 24, 8, 12, 27]
print(list(filter(lambda x:x%3==0,foo))) #筛选x%3==0 的元素
print(list(map(lambda x:x*2+10,foo)))    #遍历foo 每个元素乘2+10 再输出
print(reduce(lambda x,y:x+y,foo))        #返回每个元素相加的和