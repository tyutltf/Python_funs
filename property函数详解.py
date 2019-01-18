'''
描述
property() 函数的作用是在新式类中返回属性值。
语法
以下是 property() 方法的语法:
class property([fget[, fset[, fdel[, doc]]]])
参数
fget -- 获取属性值的函数
fset -- 设置属性值的函数
fdel -- 删除属性值函数
doc -- 属性描述信息
返回值
返回新式类属性
'''


class C(object):
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")


class Parrot(object):
    def __init__(self):
        self._voltage = 100000
    #装饰器写法
    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage


class D(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x