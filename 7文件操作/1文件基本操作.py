#文件操作

"""
文件的打开与关闭

打开：
open(文件名[,访问模式])
打开一个txt：
open("aaa.txt")
关闭：
f = open("aaa.txt")
f.close()

"""

"""
文件模式
r读
w写
a追加
后面加b，是以二进制
"""

"""
文件的读写

写文件
write方法：向文件写数据

f = open("a.txt",'w')
f.write("hello world")
f.close()
向文件写入数据时，如果不存在会自动创建文件并写入，如果文件存在，那么清空并写入


读文件
read方法：从文件中读取数据
定义：read(size)
size是要从文件中读取数据的长度单位为字节。
如果size未指定，那么读取全部数据

readlines方法：把整个文件中的内容进行一次性读取，返回一个列表，列表中的元素为每一行数据
readline方法：返回的是一个字符串对象，保存当前行的内容

代码：
fo = open("runoob.txt", "r")
print("文件名为: ", fo.name)
line = fo.readline()
print("读取第一行 %s" %line)
line = fo.readline()
print("读取第2行: %s" %line)
line = fo.readline()
print("读取第3行: %s" %line)
fo.close()
"""

