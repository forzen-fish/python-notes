#元组列表&字典

"""
列表：python中的一种数据结构，可以存储不同类型的数据
创建方式： 列表名 = [变量1，变量2，...，变量n]
列表的索引也是从0开始
列表可以套娃
如：
list_a = ['a',1,[1,'a']]
list_a[0]--->'a'
"""

"""
列表的循环遍历
使用for和while循环遍历列表
代码1（使用for）：
name = ['c','h','e','n','l','u']
for a in name:
    print(a)

代码2（使用while）：
i=0
name = ['c','h','e','n','l','u']
while i<len(name):
    print(name[i])
    i+=1

"""

"""
列表操作1
append：向列表末尾插入元素
使用：
name = ['c','h','e','n','l','u']
name.append("wangyu")
print(name)
name--->['c', 'h', 'e', 'n', 'l', 'u', 'wangyu']
"""

"""
列表操作2：
extend:将一个列表中的元素全部添加到另一个列表
name1 = ["chen","lu"]
name2 = ["wang","yu"]
name1.extend(name2)
print(name1)
print(name2)
name1--->['chen', 'lu', 'wang', 'yu']
name2--->['wang', 'yu']
"""


