'''
map()函数
map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，
并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。

例如，对于list [1, 2, 3, 4, 5, 6, 7, 8, 9]
如果希望把list的每个元素都作平方，就可以用map()函数：

因此，我们只需要传入函数f(x)=x*x，就可以利用map()函数完成这个计算：
'''
list=[1,2,3,4,5,6,7,8,9]
def f(x):
    return x*x
list1=map(f,list)
print(list1)
for i in list1:
    print(i)

'''
注意：map()函数不改变原有的 list，而是返回一个新的 list。

利用map()函数，可以把一个 list 转换为另一个 list，只需要传入转换函数。

由于list包含的元素可以是任何类型，因此，map() 不仅仅可以处理只包含数值的 list，
事实上它可以处理包含任意类型的 list，只要传入的函数f可以处理这种数据类型。

任务
假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，
请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的
'''
def format_name(s):
    s1=s[0:1].upper()+s[1:].lower()
    return s1
names=['adam', 'LISA', 'barT']
print (map(format_name, names))  #python2 这样写可以直接输出列表
for i in map(format_name,names):
    print(i)                      #python3 得这样写才可以