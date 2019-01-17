'''
在python3中如果使用reduce需要先导入

from functools import reduce

reduce函数，reduce函数会对参数序列中元素进行累积。

reduce函数的定义：
reduce(function, sequence [, initial] ) -> value
function参数是一个有两个参数的函数，reduce依次从sequence中取一个元素，
和上一次调用function的结果做参数再次调用function。
第一次调用function时，如果提供initial参数，
会以sequence中的第一个元素和initial作为参数调用function，
否则会以序列sequence中的前两个元素做参数调用function。
'''

from functools import reduce
lst=[1,2,3,4,5,6]
def f(x,y):
    return x+y
print(reduce(f,lst))

'''
过程1+2+3+4+5+6=21
'''

print(reduce(lambda x,y:x*y,lst))
# 运行过程为1*2*3*4*5*6=720

#来个稍微复杂的
print(reduce(lambda x,y:x*y+1,lst))

'''
运算步骤：1*2+1=3
         3*3+1=10
         10*4+1=41
         41*5+1=206
         206*6+1=1237
'''

#再说说有初始化值的情况, 这个时候就不是取列表的前两项, 而是取初始值为第一个,
# 序列的第一个元素为第二个元素,开始进行lambda函数的应用计算.
print(reduce(lambda x,y:x+y,lst,5))

'''
计算步骤：5+1=6
         6+2=8
         8+3=11
         11+4=15
         15+5=20
         20+6=26
'''
