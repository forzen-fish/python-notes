"""
字符串输入
input()：从标准输入中读取一行文本，默认标准输入为键盘
"""

"""
字符串的存储方式：
python不支持单字符，‘a’，同样作为字符串使用
访问字符串中的值，需要通过访问字符串下标
如：
当：name='chenlu'
访问name[0]时，就会返回c
字符串从0开始排序
"""

"""
字符串切片
[起始:结束:间隔]

name='chenlu'
name[0:3]   取0到2--->che
name[3:5]   取3到4--->nl
name[1:-1]  取1到倒数第二个--->henl
name[2:]    取2到最后一个--->enlu
name[::-2]  从后往前，间隔2，取字符--->unh
"""


"""
字符串内建函数
常用：
find(sub[,start[,end]]):检测sub是否在字符串中
语法：str.find(sub[,start[,end]])

index(sub[,start[,end]]):功能与find一样，但是错误会报错
语法：str.index(sub[,start[,end]])

count(sub[,start[,end]]):统计出现的次数
语法：str.count(sub[,start[,end]])

replace(old,new[,count]):替换字符串，次数不超过count次
语法：str.~

split(sep = None,maxsplit=-1):通过指定分隔符对字符串切片，maxsplit若有指定则分割maxsplit个字符
sep：分隔符
maxsplit：次数
语法：str.~


"""

