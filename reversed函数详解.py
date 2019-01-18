'''
描述
reversed 函数返回一个反转的迭代器。

语法
以下是 reversed 的语法:
reversed(seq)
参数
seq -- 要转换的序列，可以是 tuple, string, list 或 range。
返回值
返回一个反转的迭代器。

1 reversed(seq)
2 返回一个逆序的iterator对象。参数seq必须是一个包含__reversed__()方法的对象或支持序列操作(__len__()和__getitem__())
3 该函数是2.4中新增的
'''

str='wasdqwer'
print(list(reversed(str)))      #输出 ['r', 'e', 'w', 'q', 'd', 's', 'a', 'w']

tuple=('r', 'e', 'w', 'q', 'd', 's', 'a', 'w')
print(list(reversed(tuple)))    #输出 ['w', 'a', 's', 'd', 'q', 'w', 'e', 'r']

seqRange = range(5, 9)
print(list(reversed(seqRange)))  #输出 [8, 7, 6, 5]

seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))   #输出 [5, 3, 4, 2, 1]

a=[1,2,3,4,5,6]
b=reversed(a)
print(b)                #输出  <list_reverseiterator object at 0x0000023E2A448748>  显示为一个迭代器
print(list(b))          #输出  [6, 5, 4, 3, 2, 1]
print(list(b))          #输出  []

#由此可知：reversed（）返回的是一个迭代器对象，只能进行一次循环遍历。显示一次所包含的值！
