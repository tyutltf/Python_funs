'''
描述
sum() 方法对系列进行求和计算。
语法
以下是 sum() 方法的语法:
sum(iterable[, start])
参数
iterable -- 可迭代对象，如：列表、元组、集合。
start -- 指定相加的参数，如果没有设置这个值，默认为0。
返回值
返回计算结果
'''

print(sum([0,1,2]))              # 列表总和 3
print(sum((2,3,4),1))            # 元组计算总和后再加 1
print(sum([2,3,4,5,6],8))        # 列表计算总和后再加 2

a = list(range(1,11))
b = list(range(1,10))
c = sum([item for item in a if item in b])
print(c)                         #输出 45