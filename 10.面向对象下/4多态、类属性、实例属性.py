"""
多态
在python中，指不考虑对象类型的情况下使用对象

代码：
class 水果:
    def 打印(self):
        print("这是一个水果")

class 苹果(水果):
    def 打印(self):
        print("这是一个苹果")

class 桃子(水果):
    def 打印(self):
        print("这是一个桃子")

def func(temp):
    temp.打印()

a = 苹果()
func(a)
b = 桃子()
func(b)


当传递苹果时调用苹果的打印
当传递桃子时调用桃子的打印
"""

"""
类属性和实例属性

类属性：
class Cat(object):
    number = 0#类属性

实例属性：
def __init__(self):
    self.age = 1#实例属性
    
对象（类的实例）可以访问类属性
常用类访问类属性
如果类属性和实例属性的名字相同，通过对象访问属性时会获取实例属性对应的值，通过类访问的会获得类属性的值


"""