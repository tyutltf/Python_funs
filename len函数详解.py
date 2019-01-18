'''
描述
Python len() 方法返回对象（字符、列表、元组等）长度或项目个数。
语法
len()方法语法：
len( s )
参数
s -- 对象。
返回值
返回对象长度。
'''
str1='ltf1234'
print(len(str1))    #输出 7

list1=[1,2,3,4,5,6,7,8]
print(len(list1))   #输出 8

for i in range(len(list1)):
    print(i)        #依次输出1-8

dict = {'num':777,'name':"anne"}
print(len(dict))    #输出 2

#参考博客 https://www.cnblogs.com/101718qiong/p/7542193.html