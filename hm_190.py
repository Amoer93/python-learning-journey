#字符串定义，遇到需要增加特殊字符，可以用\+字符来实现
from itertools import count

str1 = "我的名字是\"大的西瓜\""
print(str1)
key =str1[5]
print(key)

# 用for循环把每个小的字符提取出来
for char in str1:
    print(char)

#len 函数
print(len(str1))

#count 数某一元素出现多少次
print(str1.count("的"))

#取得索引，index
print(str1.index("的"))

#可调用的功能
str1.