'''
all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
元素除了是 0、空、FALSE 外都算 TRUE。
语法
以下是 all() 方法的语法:
all(iterable)
参数
iterable -- 元组或列表。
返回值
如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
注意：空元组、空列表返回值为True，这里要特别注意。
'''
print(all(['a','b','c','']))   #列表存在一个为空的元素，返回False
print(all(['a','b','c','d']))  #列表都有元素，返回True
print(all([0,1,2,3,4,5,6]))    #列表里存在为0的元素 返回False

print(all(('a','b','c','')))   #元组存在一个为空的元素，返回Fasle
print(all(('a','b','c','d')))  #元组都有元素，返回True
print(all((0,1,2,3,4,5)))      #元组存在一个为0的元素，返回Fasle

print(all([]))  #空列表返回 True
print(all(()))  #空元组返回 True