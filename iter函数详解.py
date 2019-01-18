'''
描述
iter() 函数用来生成迭代器。
语法
以下是 iter() 方法的语法:
iter(object[, sentinel])
参数
object -- 支持迭代的集合对象。
sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object。
打开模式
返回值
迭代器对象。

1 iter(o[, sentinel])
2 返回一个iterator对象。该函数对于第一个参数的解析依赖于第二个参数。
3 如果没有提供第二个参数，参数o必须是一个集合对象，支持遍历功能（__iter__()方法）或支持序列功能（__getitem__()方法），
4 参数为整数，从零开始。如果不支持这两种功能，将处罚TypeError异常。
5 如果提供了第二个参数，参数o必须是一个可调用对象。在这种情况下创建一个iterator对象，每次调用iterator的next()方法来无
6 参数的调用o，如果返回值等于参数sentinel，触发StopIteration异常，否则将返回该值。
'''

lst = [1,2,3,4,5,6,7]
for i in iter(lst):
    print(i)      #输出1,2,3,4,5,6,7


class counter:
    def __init__(self, _start, _end):
        self.start = _start
        self.end = _end
    def get_next(self):
        s = self.start
        if(self.start < self.end):
            self.start += 1
        else:
            raise StopIteration
        return s

c = counter(1, 5)
iterator = iter(c.get_next, 3)
print(type(iterator))       #返回 <class 'callable_iterator'>
for i in iterator:
    print(i)                #输出 1  2


#参考博客 https://www.cnblogs.com/yitouniu/p/5243136.html