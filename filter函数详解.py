'''
filter() 函数是一个对于可迭代对象的过滤器，过滤掉不符合条件的元素，
返回的是一个迭代器，如果要转换为列表，可以使用 list() 来转换。
该函数接收两个参数，第一个为函数的引用或者None，第二个为可迭代对象，
可迭代对象中的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到迭代器中
下面看下fiter()的用法：
'''

my_list=[1,2,'',3,4,'6',' ']
new_list=list(filter(None,my_list))
print(new_list)
#None 函数 过滤掉'' 而不是过滤掉空字符串

def is_oushu(x):
    return x%2==0
new_list=list(filter(is_oushu,list(range(1,11))))
print(new_list)
#过滤掉不是偶数的数

a=[1,2,3,4,5,6,2,2,2,]
print(list(filter(lambda x:x!=2,a)))
#筛选出列表里所有的不是 2  的元素