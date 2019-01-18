'''
描述
set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
语法
set 语法：
class set([iterable])
参数说明：
iterable -- 可迭代对象对象；
返回值
返回新的集合对象。
'''

a=set('www.baidu.com')
b=set('www.gogle.com')      #重复的元素被删除 元素唯一 可以用来去重
print(a)                    #输出   {'u', '.', 'm', 'c', 'w', 'd', 'i', 'a', 'o', 'b'}
print(b)                    #输出   {'.', 'm', 'e', 'c', 'w', 'o', 'l', 'g'}

print(a&b)                  #交集 {'m', 'c', 'w', '.', 'o'}
print(a|b)                  #并集 {'m', 'c', 'i', 'w', 'b', 'd', 'u', 'g', 'e', 'a', '.', 'o', 'l'}
print(a-b)                  #差集 {'i', 'b', 'd', 'u', 'a'}


#1.比较
se = {11, 22, 33}
be = {22, 55}
temp1 = se.difference(be)        #找到se中存在，be中不存在的集合，返回新值
print(temp1)        #{33, 11}
print(se)        #{33, 11, 22}

temp2 = se.difference_update(be) #找到se中存在，be中不存在的集合，覆盖掉se
print(temp2)        #None
print(se)           #{33, 11},


#2.删除
se = {11, 22, 33}
se.discard(11)
se.discard(44)  # 移除不存的元素不会报错
print(se)

se = {11, 22, 33}
se.remove(11)
#se.remove(44)  # 移除不存的元素会报错
print(se)

se = {11, 22, 33}  # 移除末尾元素并把移除的元素赋给新值
temp = se.pop()
print(temp)  # 33
print(se) # {11, 22}


#3.取交集
se = {11, 22, 33}
be = {22, 55}

temp1 = se.intersection(be)             #取交集，赋给新值
print(temp1)  # 22
print(se)  # {11, 22, 33}

temp2 = se.intersection_update(be)      #取交集并更新自己
print(temp2)  # None
print(se)  # 22


#4.判断
se = {11, 22, 33}
be = {22}

print(se.isdisjoint(be))        #False，判断是否不存在交集（有交集False，无交集True）
print(se.issubset(be))          #False，判断se是否是be的子集合
print(se.issuperset(be))        #True，判断se是否是be的父集合


#5.合并
se = {11, 22, 33}
be = {22}

temp1 = se.symmetric_difference(be)  # 合并不同项，并赋新值
print(temp1)    #{33, 11}
print(se)       #{33, 11, 22}

temp2 = se.symmetric_difference_update(be)  # 合并不同项，并更新自己
print(temp2)    #None
print(se)             #{33, 11}

#6.取并集

se = {11, 22, 33}
be = {22,44,55}

temp=se.union(be)   #取并集，并赋新值
print(se)       #{33, 11, 22}
print(temp)     #{33, 22, 55, 11, 44}


#7.更新
se = {11, 22, 33}
be = {22,44,55}

se.update(be)  # 把se和be合并，得出的值覆盖se
print(se)
se.update([66, 77])  # 可增加迭代项
print(se)


#8.集合的转换
se = set(range(4))
li = list(se)
tu = tuple(se)
st = str(se)
print(li,type(li))        #输出 [0, 1, 2, 3] <class 'list'>
print(tu,type(tu))        #输出 [0, 1, 2, 3] <class 'tuple'>
print(st,type(st))        #输出 [0, 1, 2, 3] <class 'str'>


#参考博客  https://www.cnblogs.com/whatisfantasy/p/5956775.html