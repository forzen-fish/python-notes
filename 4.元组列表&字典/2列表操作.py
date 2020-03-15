"""
insert:在列表指定位置添加元素
insert(index,object)
在指定位置index，插入object

num = [0,1,2]
num.insert(1,3)
print(num)
num--->[0, 3, 1, 2]
"""

"""
在列表中查找元素
in：存在为True,不存在为False
not in：不存在为True,存在为False

"""

"""
修改列表元素
num = [0,1,2,3]
num[1] = 2
print(num)
---->num[0,2,2,3]
"""

"""
在列表中删除元素

del:删除列表
代码1：
a = [1,2,3,4,5,6,7]
for b in a:
    print(b)
    #1234567
del a[1]
for b in a:
    print(b)
    #134567
    
pop:删除列表元素
代码2：
a = [1,2,3,4,5,6,7]
for b in a:
    print(b)
    #1234567
a.pop()
for b in a:
    print(b)
    #123456

remove：删除列表元素
a = [1,2,3,4,5,6,7]
for b in a:
    print(b)
    #1234567
a.remove(2)
for b in a:
    print(b)
    #134567
"""
a = [1,2,3,4,5,6,7]
for b in a:
    print(b)
    #1234567
a.remove(2)
for b in a:
    print(b)
    #134567






