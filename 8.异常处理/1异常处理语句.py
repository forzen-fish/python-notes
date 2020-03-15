#异常处理
"""
捕获简单异常
try:
    #语句块
except:
    #异常处理代码

当try中的语句出现错误，跳出try，执行except语句
except后可以跟错误类型，并且可以多个捕获

try:
    #语句块
except 错误类型1:
    #异常处理代码
except 错误类型2:
    #异常处理代码
...

except可以接else
当无论有无异常都需要执行语句时：
try:
    #语句块
except 错误类型1:
    #异常处理代码
except 错误类型2:
    #异常处理代码
else:
    #没有异常时执行的代码
finally:
    #终止语句

"""

"""
抛出异常
raise语句
基本格式：
raise 异常类/异常类对象/空（重新引发刚刚发生的异常）

1.类名引发异常
raise IndexError
2.使用异常类的实例引发异常
index = IndexError()
raise index
3.传递刚刚发生的异常
try:
    raise IndexError
except:
    raise
4.添加错误信息
raise IndexError("错误信息")
5.异常引发异常
try:
    number#nameerror
except Exception as exception:
    raise IndexError("提示信息") from exception
"""


