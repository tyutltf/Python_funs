'''
enumerate是翻译过来是枚举的意思，看下它的方法原型：
enumerate(sequence, start=0)，返回一个枚举对象。
sequence必须是序列或迭代器iterator，或者支持迭代的对象。
enumerate()返回对象的每个元素都是一个元组，
每个元组包括两个值，一个是计数，一个是sequence的值，
计数是从start开始的，start默认为0。
---------------------
'''
a=["q","w","e","r"]
c=enumerate(a)
for i in c:
    print(i)

'''
输出如下:
(0, 'q')
(1, 'w')
(2, 'e')
(3, 'r')
'''

a=["w","a","s","d"]
#这里加了个参数2，代表的是start的值
c=enumerate(a,2)
for i in c:
    print(i)
'''
输出如下：
(2, 'w')
(3, 'a')
(4, 's')
(5, 'd')
'''

a=["q","w","e","r"]
#创建一个空字典
b=dict()
#这里i表示的是索引，item表示的是它的值
for i,item in enumerate(a):
    b[i]=item
print(b)   #输出 {0: 'q', 1: 'w', 2: 'e', 3: 'r'}

for i,j in enumerate('abc'):
    print(i,j)
#输出结果
# 0 a
# 1 b
# 2 c