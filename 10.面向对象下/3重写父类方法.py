"""
重写父类方法与调用父类方法
对父类中继承来的方法进行重写，使子类中的方法覆盖掉跟父类同名的方法。
子类中重写的方法要和父类被重写的方法具有相同的参数列表

代码：
class people:
    def __init__(self):
        print("hi")
    def say_hello(self):
        print("hello")


class China_people(people):
    def say_hello(self):
        print("你好")

class US_people(people):
    def __init__(self):
        print("hey")

Chinese = China_people()
Chinese.say_hello()

Us = US_people()
Us.say_hello()
"""


