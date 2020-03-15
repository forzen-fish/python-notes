#面向对象  OO

"""
类和对象


类由三部分组成：
类名
属性
方法
语法：
class 类名:
    属性
    方法
代码：
class Cat:
    def eat(self):
        print("吃鱼")
cat类，一个eat方法，方法必须显式的声明一个self参数代表类的实例（对象）

根据类创建对象
对象名 = 类名()
cat1 = Cat()
可以通过对象访问类的属性和方法
添加/修改新属性：
对象名.属性名 = 值
cat1.color = "black"
"""

"""
构造方法：
当创建类的实例的时候，系统会自动调用构造方法，从而实现对类的初始化操作
__init__

代码：
class Car:
    def __init__(self):#一开始这里就执行了
        self.color = "black"
        print("一开始这里就执行了")
    def pri(self):
        print("这是一个%s的车"%(self.color))
car1 = Car()
car1.pri()
"""


