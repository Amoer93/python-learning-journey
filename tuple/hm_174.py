info_tuple = ("Zhangsan",1,19)

#想知道某index的内容
print(info_tuple[2])

#已知数据内容，但是要知道index
print(info_tuple.index("Zhangsan"))

#已知内容，需要知道出现的次数
print(info_tuple.count("Zhangsan"))

#for 可以用来遍阅所有非数字格式的变量
#例如list，tuple，dir，string
list_combin = ["zhangsan",1,"wangwu"]
for item in list_combin:
    print(f"the student is {item}")


student1 = ("zhangsan",1,19)
student2 = ("wangwu",0,18)
student3 = ("zhaoliu",1,20)

student = [student1,student2,student3]

#for name, gender, age in student:
#   print(f"{name} is {gender} and {age} years old")
print("%s is %d and %0.0f years old"%(student[0]))


number_list = [1,2,3,4,5,6,7,8,9]
print(type(number_list))
number_tuple = tuple(number_list)
print(type(number_tuple))