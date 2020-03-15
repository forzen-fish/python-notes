"""
单继承
class Dog(object):
    def __init__(self,color = "white"):
        self.color = color
    def run(self):
        print("run")

class RED_Dog(Dog):
    pass

dog1 = RED_Dog("red")
dog1.run()
print(dog1.color)


父类的私有方法和私有属性是不会被子类继承的，也不能被子类访问

"""

"""
多继承
子类继承多个父类
语法格式：
class 子类(父类1,父类2...)

代码
class 陆地生物:
    def ludi(self):
        print("地上爬的")

class 水下生物:
    def shuixia(self):
        print("水里游的")

class 蛤蟆(陆地生物,水下生物):
    pass

蛤蟆1 = 蛤蟆()
蛤蟆1.shuixia()
蛤蟆1.ludi()


如果继承关系复杂，通过mro算法找到合适的类，
调用__mro__()方法可以查看先后顺序
"""
