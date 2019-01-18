'''
描述
sorted() 函数对所有可迭代的对象进行排序操作。
sort 与 sorted 区别：
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
语法
sorted 语法：
sorted(iterable, key=None, reverse=False)
参数说明：
iterable -- 可迭代对象。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
返回值
返回重新排序的列表。
'''

print(sorted([2,3,4,1,5,6]))          #输出 [1, 2, 3, 4, 5, 6]

#另一个区别在于list.sort() 方法只为 list 定义。而 sorted() 函数可以接收任何的 iterable。
print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))      #输出  [1, 2, 3, 4, 5]

#利用key进行倒序排序
example_list = [5, 0, 6, 1, 2, 7, 3, 4]
result_list = sorted(example_list, key=lambda x: x*-1)
print(result_list)                   #输出  [7, 6, 5, 4, 3, 2, 1, 0]

#要进行反向排序，也通过传入第三个参数 reverse=True：
example_list = [5, 0, 6, 1, 2, 7, 3, 4]
result_list=sorted(example_list, reverse=True)
print(result_list)                   #输出 [7, 6, 5, 4, 3, 2, 1, 0]

#sorted 的应用，也可以通过 key 的值来进行数组/字典的排序，比如
array = [{"age":20,"name":"a"},{"age":25,"name":"b"},{"age":10,"name":"c"}]
array = sorted(array,key=lambda x:x["age"])
print(array)                         #输出 [{'age': 10, 'name': 'c'}, {'age': 20, 'name': 'a'}, {'age': 25, 'name': 'b'}]