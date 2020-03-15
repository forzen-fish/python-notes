"""
变量作用域
程序变量不是在每个位置都可以访问的，访问权限决定于变量赋值的位置
遵循LEGB
LEGB：
L local 函数内的区域，包括局部变量与参数
E enclosing 外面嵌套函数的区域常见的是必报函数的外层函数
G global 全局作用域
B built-in 内建作用域

L>E>G>B

"""

"""
全局变量&局部变量
代码：
r = 100#全局变量
def aa(a,b):
    r = a+b  #局部变量
    print(r)#局部变量r
    return r
aa(100,200)
print(r)#全局变量r
输出：
300
100
"""

"""
global nonlocal关键字

global:声明全局变量(给你个代码自己体会)声明前变量可以不存在
代码：
a = 100
def aa():
    global a
    a = 200
    print(a)
aa()
print(a)

nonlocal:声明嵌套作用域变量 修饰的变量在嵌套作用域中必须存在
代码:
def aa():
    a = 100
    def bb():
        nonlocal a
        a = 200
    bb()
    print(a)
aa()
"""




