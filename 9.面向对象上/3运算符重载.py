"""
运算符重载
通过实现特定的方法使类的实例对象支持python的各种内置操作

常用运算符重载方法：
__add__、__sub__、__mut__、__div__、__mod__........

代码：加法运算符重载
class Deom:
    def __init__(self, obj):
        self.data = obj
    def __add__(self, obj):
        x = len(self.data)
        y = len(obj.data)
        max = x if x>y else y
        number_list = []
        for n in range(max):
            number_list.append(self.data[n] + obj.data[n])
        return Deom(number_list)
a = Deom([1,2,3])
b = Deom([10,20,30])
sum = a+b
print(sum.data)
[11, 22, 33]
"""



