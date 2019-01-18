'''
python staticmethod 返回函数的静态方法。
该方法不强制要求传递参数，如下声明一个静态方法：
class C(object):
    @staticmethod
    def f(arg1, arg2, ...):
        ...
以上实例声明了静态方法 f，类可以不用实例化就可以调用该方法 C.f()，当然也可以实例化后调用 C().f()。
函数语法
staticmethod(function)
参数说明：
无
'''

class C(object):
    @staticmethod
    def f():
        print('hello world')
C.f()               # 静态方法无需实例化
cobj = C()
cobj.f()            # 也可以实例化后调用



class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)
a = A()
print(a.foo)               #输出 <bound method A.foo of <__main__.A object at 0x000001B5B2A51D30>>
print(a.class_foo)         #输出 <bound method A.class_foo of <class '__main__.A'>>
print(a.static_foo)        #输出 <function A.static_foo at 0x000001B5B2A55598>

#参考博客 https://www.cnblogs.com/elie/p/5876210.html