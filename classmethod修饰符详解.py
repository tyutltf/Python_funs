'''
描述
classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
语法
classmethod 语法：
classmethod
参数
无。
返回值
返回函数的类方法。
'''

class Stud:
    num=1
    def fn1(self):
        print('方法一')
    @classmethod
    def fn2(cls):
        print('方法二')   #输出 方法二
        print(cls.num)    #调用类的实例化对象
        cls().fn1()       #调用类的方法

Stud.fn2()    #输出 方法二 不需要实例化

print('===='*10)
object=Stud()
object.fn1()  #输出 方法一 需要实例化
