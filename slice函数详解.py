'''
描述
slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。
语法
slice 语法：
class slice(stop)
class slice(start, stop[, step])
参数说明：
start -- 起始位置
stop -- 结束位置
step -- 间距
返回值
返回一个切片对象。
实例
'''

myslice=slice(5)      #设置一个 截取五个元素的切片
print(myslice)        #输出 slice(None, 5, None)

arr=list(range(10))
print(arr)            #输出 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr[myslice])   #输出 [0, 1, 2, 3, 4]

print(arr[3:6])       #输出 [3, 4, 5]