"""
不定长参数
格式：
def 函数名([formal_args,]*args,**kwargs):
    函数体
return 表达式

formal_args：形参
*args,**kwargs：不定长参数

举例说明：
def e(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
e(11,22,33,44,55,66,77,m=66,n=77)

11
22
(33, 44, 55, 66, 77)
{'m': 66, 'n': 77}
"""

"""
函数返回值
在函数完成后，返回给调用者的结果
使用return完成
"""

"""
函数的四种类型
函数无参数，无返回值
函数无参数，有返回值
函数有参数，无返回值
函数有参数，有返回值
"""

"""
函数的嵌套调用
举例：
def p():
    print("p")
def q():
    print("q")
    p()
q()

q
p
"""



