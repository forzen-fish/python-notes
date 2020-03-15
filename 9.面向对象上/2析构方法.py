"""
带参数的构造方法
class Car:
    def __init__(self,color):#一开始这里就执行了
        self.color = color
        print("一开始这里就执行了")
    def pri(self):
        print("这是一个%s的车"%(self.color))
car1 = Car("black")
car2 = Car("white")
car1.pri()
car2.pri()
"""

"""
析构方法
__def__()方法
del 对象  ：删除对象
删除时自动调用__def__()方法
class Car:
    def __init__(self,color):#一开始这里就执行了
        self.color = color
        self.num = 23
        print("一开始这里就执行了")
    def __del__(self):
        print("del")
car = Car("red")
del car
print(car.num)
"""

"""
self的使用
表示对象自身，当某个对象调用时方法时，解释器会把这个对象作为第一参数传给self

"""


"""
索引和分片重载
__getitem__：索引、分片
__setitem__：索引赋值
__delitem__：索引和分片删除.
用到再说
"""




