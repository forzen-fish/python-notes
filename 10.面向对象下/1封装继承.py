#面向对象
"""
三大特性：封装，继承，多态
"""

"""
封装（隐藏数据和保护属性）
隐藏属性，方法，与方法实现细节的过程称为封装。
保护内部属性，避免外部随意赋值
方式：
把属性定义为私有属性，即在属性名的前面加上两个下划线
添加可以供外界调用的两个方式，分别用于设置或者获取属性值

代码：
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def set_age(self,new_age):
        if new_age>0 and new_age<=120:
            self.__age = new_age
    def get_age(self):
        return self.__age

a = Person("cl",18)
a.set_age(19)
print(a.get_age())
print(a.__age)#直接访问与直接设置会出现错误
"""

"""
继承
在一个现有类的基础上构建一个新类，新类被称作子类，原类被称为父类，子类会自动拥有父类的属性和方法
语法：
class 子类名(父类名):

假设A是B的父类
class A(object):
class B(A):
"""


"""
定义类时，如果不标注出父类，默认继承自object
object是类的父类，是类的子类的爷爷类
"""





