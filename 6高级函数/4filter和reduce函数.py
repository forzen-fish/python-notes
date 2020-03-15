"""
filter函数：
定义：filter(function,iterable)
function可以是函数名或None，只接受一个参数且返回值为布尔值
代码：
f = lambda x:x%2
r = filter(f,[1,2,3,4,5,6,7,8,9])
print(r)
print(list(r))
---[1, 3, 5, 7, 9]
因为1  3  5  7  9，对2求余数为1，布尔值为真，所以返回此列表
"""

"""
reduce函数
对参数迭代器中的元素进行累积
定义：functools.reduce(function,iterable[,initializer])
function是带有两个参数的函数，第二个参数iterable是一个迭代器对象，initializer表示固定的初始值
reduce函数会依次从迭代器中取出每个元素，和上一次调用function的结果作为参数再次调用function
使用前需要引入
参数可以用字符串
from functools import reduce
代码：
from functools import reduce
f = lambda x,y:x+y
r = reduce(f,[1,2,3,4,5,6])
print(r)


"""
