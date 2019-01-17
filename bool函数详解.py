'''
描述
bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。
bool 是 int 的子类。
语法
以下是 bool() 方法的语法:
class bool([x])
参数
x -- 要进行转换的参数。
返回值
返回 Ture 或 False。
'''
print(bool(0))         #返回False
print(bool(1))         #返回True
print(bool(True))      #返回True
print(bool(False))     #返回False
print(bool(''))        #返回False


#0,False,'',  空字符串返回Fasle