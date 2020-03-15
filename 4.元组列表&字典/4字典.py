"""
字典
存储多个数据，同时精确定位
格式：
字典名 = {'key(键)':value(值),...}
"""

"""
根据键访问值
1:
dict = {'a':2,'b':'c'}
print(dict['a'])#2
print(dict['b'])#c

2:
dict = {'a':2,'b':'c'}
a = dict.get('c')#不存在c返回None
b = dict.get('c',132)#如果不存在c，返回132
print(a)#None
print(b)#132

"""

"""
修改字典中的元素
dict = {'a':2,'b':'c'}
dict['a'] = 5
print(dict)

"""


"""
添加字典元素
当使用  变量名[键] = 数据  时，如果键不存在，就会添加上
"""

"""
删除字典元素
使用del clear两个命令实现
del：
num = {'a':1,'b':2,'c':3}
del num['c']
print(num)
{'a': 1, 'b': 2}

clear:
num = {'a':1,'b':2,'c':3}
num.clear()
print(num)
{}
"""


