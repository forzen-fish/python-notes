"""
if嵌套：
if ...:
    if ...:
        if ...:
注意缩进
"""

"""
循环结构
while:
格式：
while 条件表达式:
    条件表达式为真时，执行缩进语句

for:
格式:
for 变量 in 序列:
    循环语句

for i in range(start,end):
    循环语句

range函数能自动生成数字序列，循坏开始时，i为start，直到i=end时结束

循环也是可以嵌套的
"""

"""
其他语句：break,continue
注意：只能在循环中使用，作用于最近的循环
break语句：用于结束循环
代码1：
for i in [1,2,3,4,5,6]:
    print(i)
    if i==3:
        break
        print("这里不打印")
    print("当i=3时，这里也不打印，所以这里只打印两遍")
print("跳出循环了")

continue:结束本次循环，接着执行下一次
代码2:
for i in [1,2,3,4,5]:
    print(i)
    if i==3:
        continue
    print("i=3时，这里被跳过一次循环")
"""