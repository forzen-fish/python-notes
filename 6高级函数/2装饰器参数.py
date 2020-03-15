"""
多个装饰器
def zhuangshiqi1(hanshu):
    print("zhuangshi1_ing")
    def inner1():
        print("inner1函数")
        hanshu
    return inner1

def zhuangshiqi2(hanshu):
    print("zhuangshi2_ing")
    def inner2():
        print("inner2函数")
        hanshu
    return inner2

@zhuangshiqi1
@zhuangshiqi2
def aaa():
    print("aaa")

aaa()

注意：不要出现test，不然会有蜜汁bug
"""

"""
装饰器装饰有参函数
方法1（不能通用,装饰器几个参数，函数几个参数）：
def zhuanshiqi(f):
    def inner(a,b):
        f(a,b)
    return inner

@zhuanshiqi
def aa(a,b):
    print(a)
    print(b)

aa(1,44)

方法2使用不定长参数：
def zhuanshiqi(f):
    def inner(*arg,**kwargs):
        f(*arg,**kwargs)
    return inner
#下面省略
"""


