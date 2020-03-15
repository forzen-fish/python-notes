"""
文件的定位读写
使用tell方法获取文件当前的读写位置
使用seek方法定位到文件的指定位置
seek(offset[,whence])
offset:需要移动的字节数
whence:表示方向，三个参数值：
1：0 默认参数值，从文件起始位置开始偏移
2: 1 从文档当前位置偏移
3：2 从未当末尾开始偏移

"""

"""
需要os模块

文件的重命名
os.rename("原名","新名")

文件的删除
os.remove("文件路径")

创建文件夹
os.mkdir("文件夹名称")
获取当前目录
os.getcwd()
改变默认目录
os.csdir(目录)
获取目录列表
os.listdir(路径)
删除文件夹
os.rmdir(文件夹名称)

"""

