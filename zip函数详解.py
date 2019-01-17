#zip函数接受任意多个可迭代对象作为参数,将对象中对应的元素打包成一个tuple,然后返回一个可迭代的zip对象.
#这个可迭代对象可以使用循环的方式列出其元素
#若多个可迭代对象的长度不一致,则所返回的列表与长度最短的可迭代对象相同.

#1.用列表生成zip对象
x=[1,2,3]
y=[4,5,6]
z=[7,8,9]
h=['a','b','c','d']
zip1=zip(x,y,z)
print(zip1)
for i in zip1:
    print(i)

zip2=zip(x,y,h)
for i in zip2:
    print(i)

zip3=zip(h)
for i in zip3:
    print(i)

zip4=zip(*h*3)
for i in zip4:
    print(i) #这是干啥哟。。

print('==*=='*10)
#2.二维矩阵变换
l1=[[1,2,3],[4,5,6],[7,8,9]]
print(l1)
print([[j[i] for j in l1] for i in range(len(l1[0])) ])
zip5=zip(*l1)
for i in zip5:
    print(i)