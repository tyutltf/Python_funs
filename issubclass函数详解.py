'''
描述
issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类。
语法
以下是 issubclass() 方法的语法:
issubclass(class, classinfo)
参数
class -- 类。
classinfo -- 类。
返回值
如果 class 是 classinfo 的子类返回 True，否则返回 False。
'''


class A:
    pass

class B(A):
    pass

class C(A):
    pass

print(issubclass(B, A))  # 返回 True
print(issubclass(C, A))  # 返回 True
print(issubclass(C, B))  # 返回 False

#2.class参数是classinfo的子类，并且classinfo是元组
print(issubclass(C, (A, object)))                #返回  True
print(issubclass(C, (A, int, object)))           #返回  True
print(issubclass(C, (int, str)))                 #返回 False
print(issubclass(C, (int, str, type)))           #返回 False

#print(issubclass(C, (1, A)))
#报错 TypeError: issubclass() arg 2 must be a class or tuple of classes

#参考简书 https://www.jianshu.com/p/4c425bbdd773