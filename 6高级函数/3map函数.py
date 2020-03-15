"""
装饰器修饰带有返回值的函数

def f(a):
    def inner():
        return a()
    return inner

调用时可以得到返回值

"""

"""
带参数的装饰器
加强装饰
def fun(args):
    def func(a):
        def func_in():
            print(args)
            a()
        return func_in
    return func

@fun("abcdefg")
def abc():
    print('test')

abc()

"""

"""
常见python内置函数

map函数
定义：map(function,iterable,...)
第一个参数是函数名(匿名函数也可以)，第二个参数可以是序列、支持迭代的容器或迭代器。
当调用map，iterable每个元素都会进入函数function执行，返回的结果保存到一个迭代器对象中
代码：
def aa(a):
    c = a*5
    return c
r = map(aa,[1,2,5,6,3,7])
print(r)
print(list(r))
"""


