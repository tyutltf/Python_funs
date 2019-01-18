'''
list()　　列表构造函数

1 list([iterable])
2 list的构造函数。参数iterable是可选的，它可以是序列，支持编译的容器对象，或iterator对象。
3 该函数创建一个元素值，顺序与参数iterable一致的列表。如果参数iterable是一个列表，将创建
4 列表的一个拷贝并返回，就像语句iterables[:]。
'''

list=[1,2,3,4,5,6,7,8,9]    #构建列表
print(list)                 #输出 [1,2,3,4,5,6,7,8,9]

list.append(10)             #列表追加 10
print(list)                 #输出 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list.insert(2,18)           #在列表索引为2 的位置 插入 18 其余的后移
print(list)                 #输出 [1, 2, 18, 3, 4, 5, 6, 7, 8, 9, 10]

print(list.count(1))        #输出 列表里1 的数量

list2=[-1,-2,-3]
list.extend(list2)          #列表追加列表
print(list)                 #输出 [1, 2, 18, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3]

list.remove(1)              #删除列表里的第一个1
print(list)                 #输出 [2, 18, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3]

list.sort()                 #列表排序
print(list)                 #输出 [-3, -2, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18]

list.reverse()              #列表反转
print(list)                 #输出 [18, 10, 9, 8, 7, 6, 5, 4, 3, 2, -1, -2, -3]

print(max(list))            #输出列表最大值 18
print(min(list))            #输出列表最小值 -3

list3=[1,2,3,'q','a','s']
#print(max(list3))           #报错 >' not supported between instances of 'str' and 'int'
#print(min(list3))           #报错 >' not supported between instances of 'str' and 'int'
