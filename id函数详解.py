'''
id() 函数用于获取对象的内存地址。
语法
id 语法：
id([object])
参数说明：
object -- 对象。
返回值
返回对象的内存地址。
'''
str='zhangsan'
print(id(str))  #输出 1556579882544  动态分配 id  每一次会改变

b=1
print(id(b))    #输出 1597205568

'''
id方法的返回值就是对象的内存地址。

python2中会为每个出现的对象分配内存，哪怕他们的值完全相等（注意是相等不是相同）。
如执行a=2.0，b=2.0这两个语句时会先后为2.0这个Float类型对象分配内存，
然后将a与b分别指向这两个对象。所以a与b指向的不是同一对象

python3中 值相等的变量 内存一样 如下图所示
'''

a=10.21
b=10.21
print(id(a))       #输出2036826247912
print(id(b))       #输出2036826247912
print(a is b)      #输出  True
print(a == b)      #输出  True

'''
id 函数 涉及到 浅拷贝和深拷贝的相关知识

深copy和浅copy
深copy新建一个对象重新分配内存地址，复制对象内容。

浅copy不重新分配内存地址，内容指向之前的内存地址。
浅copy如果对象中有引用其他的对象，如果对这个子对象进行修改，子对象的内容就会发生更改。
'''

import copy

#这里有子对象
numbers=['1','2','3',['4','5']]
#浅copy
num1=copy.copy(numbers)
#深copy
num2=copy.deepcopy(numbers)

#直接对对象内容进行修改
num1.append('6')

#这里可以看到内容地址发生了偏移，增加了偏移‘6’的地址
print('numbers:',numbers)
print('numbers memory address:',id(numbers))
print('numbers[3] memory address',id(numbers[3]))
print('num1:',num1)
print('num1 memory address:',id(num1))
print('num1[3] memory address',id(num1[3]))


num1[3].append('6')

print('numbers:',numbers)
print('num1:',num1)
print('num2',num2)
'''

输出：
numbers: ['1', '2', '3', ['4', '5']]
numbers memory address: 1556526434888
numbers memory address 1556526434952
num1: ['1', '2', '3', ['4', '5'], '6']
num1 memory address: 1556526454728
num1[3] memory address 1556526434952
numbers: ['1', '2', '3', ['4', '5', '6']]
num1: ['1', '2', '3', ['4', '5', '6'], '6']
num2 ['1', '2', '3', ['4', '5']]
'''

#参考博客 https://www.cnblogs.com/dplearning/p/5998112.html
#参考博客 https://www.cnblogs.com/JackFu/p/8014762.html