"""
assert语句
断言语句，可以当做有条件的raise语句
格式：
assert 逻辑表达式[,data]
相当于：
if not 逻辑表达式:
    raise AsswertionError(data)
assert 1==3,"logicerror"
--->AssertionError: logicerror

"""


"""
自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)
后面再细说
"""

"""
预定义清理
with语句
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
如果代码出现问题，f也会正常关闭
我感觉这里八辈子用不着，讲了的话再说
"""
