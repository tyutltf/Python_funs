'''
描述
frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
语法
frozenset() 函数语法：
class frozenset([iterable])
参数
iterable -- 可迭代的对象，比如列表、字典、元组等等。
返回值
返回新的 frozenset 对象，如果不提供任何参数，默认会生成空集合。
'''

a=frozenset(range(10))
print(a)
#输出  frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

b=frozenset('ltftyut1234')
print(b)
#输出  frozenset({'2', '4', 't', 'f', '1', '3', 'l', 'y', 'u'})

# 1 frozenset([iterable])
# 2 set和frozenset最本质的区别是前者是可变的，后者是不可变的。当集合对象会被改变时（例如删除，添加元素），只能使用set，
# 3 一般来说使用fronzet的地方都可以使用set。
# 4 参数iterable：可迭代对象。