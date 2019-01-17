'''
any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
元素除了是 0、空、FALSE 外都算 TRUE。
语法
以下是 any() 方法的语法:
any(iterable)
参数
iterable -- 元组或列表。
返回值
如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true。
'''
print(any(['a','b','c','']))   #列表存在一个为空的元素，返回True
print(any(['a','b','c','d']))  #列表都不为空，返回True
print(any([0,'',False]))       #列表里的元素全为  0,'',False  返回False

print(any(('a','b','c','')))   #元组存在一个为空的元素，返回True
print(any(('a','b','c','d')))  #元组都有元素，返回True
print(any((0,'',False)))       #元组里的元素全为  0,'',False  返回False

print(any([]))  #空列表返回 False
print(any(()))  #空元组返回 False