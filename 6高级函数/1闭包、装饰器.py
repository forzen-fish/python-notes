"""
高级函数
"""

"""
闭包
满足下面三个条件的函数就被成为闭包
1：存在于嵌套关系的函数中
2：嵌套的内部函数引用了外部函数的变量
3：嵌套的外部函数会将内部函数名作为返回值返回

代码：
def out(s = 0):
    c = [s]#2
    def inn():#1
        c[0] += 1#2
        return c[0]
    return inn()#3
q = out(5)
print(q)
--->6
"""

"""
装饰器
在不改动其他函数的前提下，对函数的功能进行扩充
通常用于：
引入日志、函数执行时间统计、执行函数前预备处理、执行函数后清理功能、权限校验、缓存
装饰器的语法是以@开头
代码：
def zhuangshiqi(hanshu):
    print("zhuangshi_ing")
    def inner():
        print("inner函数")
        hanshu
    return inner

@zhuangshiqi
def test():
    print("test")

test()

想要装饰就@一下装饰器
"""


def zhuangshiqi(hanshu):
    print("zhuangshi_ing")
    def inner():
        print("inner函数")
        hanshu
    return inner

@zhuangshiqi
def test():
    print("test")

test()


