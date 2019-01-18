'''
描述
dict() 函数用于创建一个字典。
语法
dict 语法：
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
参数说明：
**kwargs -- 关键字
mapping -- 元素的容器。
iterable -- 可迭代对象。
返回值
返回一个字典。
'''

print(dict())   #创建空字典
dict1=dict(a='a', b='b', t='t')   #传入关键字 构建字典
print(dict1)    #输出 {'a': 'a', 'b': 'b', 't': 't'}

dict2=dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
print(dict2)    #输出 {'one': 1, 'two': 2, 'three': 3}

dict3=dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
print(dict3)     #输出 {'one': 1, 'two': 2, 'three': 3}
