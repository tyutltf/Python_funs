'''
Python3.x 中 input() 函数接受一个标准输入数据，返回为 string 类型。
注意：在 Python3.x 中 raw_input() 和 input() 进行了整合，
去除了 raw_input( )，仅保留了input( )函数，其接收任意任性输入，
将所有输入默认为字符串处理，并返回字符串类型。
函数语法
input([prompt])
参数说明：
prompt: 提示信息
'''

a=input('请输入一个数:')  #输入 10
print(a)                 #输出 10
print(type(a))           #输出 <class 'str'>
#b=a+10           #报错 TypeError: must be str, not int
b=int(a)+10       #转换成整型
print(b)          #输出 20

a=input('请输入一个字符串:')      #输入  ltf1234
print(a)                         #输出  字符串ltf1234  可以使用字符串对应的方法
print(a.split('1'))              #输出   ['ltf', '234']  split 切割字符串 直接输出列表