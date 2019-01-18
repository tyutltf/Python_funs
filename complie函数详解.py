'''
complie()　　将字符串编译成python能识别或可以执行的代码，也可以将文字读成字符串再编译

1 compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
2 将source编译为代码或者AST对象。代码对象能过通过exec语句来执行或者eval()进行求值。
3 参数source：字符串或者AST（abstract syntax trees）对象。
4 参数filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
5 参数model：指定编译代码的种类。可以指定'exec', 'eval', 'single'。
6 参数flag和dont_inherit：这两个参数为可选参数。
'''

s="print('hello world')"
r=compile(s,'hello','exec')
print(r)

#输出结果：
#<code object <module> at 0x000002EBD335CF60, file "hello", line 1>

