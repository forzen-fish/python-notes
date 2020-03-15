"""
类方法和静态方法
类方法和静态方法都属于类的方法
"""

"""
类方法：
格式：
class 类名:
    @classmethod
    def 类方法名(cls):
        方法体

类方法的第一个参数为cls，代表定义方法的类，可以通过cls访问类的属性
可以通过对象名和类名调用类方法
类方法无法访问实例属性，但可以访问类属性

代码：
class Test(object):
    number = 0
    @classmethod
    def set_number(cls,new_number):
        cls.number = new_number

Test.set_number(250)
print(Test.number)

"""

"""
静态方法

格式：
class 类名:
    @staticmethod
    def 静态方法名():
        方法体

静态方法的参数列表没有任何参数，由于没有self，所以无法访问实例属性，同样没有cls，也无法访问属性
静态方法跟定义他的类没有直接的关系，只起到类似函数的作用

使用时，可以通过对象名和类名调用静态方法

代码：
class Test():
    @staticmethod
    def print_test():
        print("这里是静态方法")
Test.print_test()
test = Test()
test.print_test()


如果需要修改属性的值，就直接使用实例方法
如果需要修改类属性的值，就用类方法
如果是辅助功能（如打印菜单），可以考虑静态方法，可以不创建对象

其实我也不知道这里有个毛的用处，知道应该就行了

"""


