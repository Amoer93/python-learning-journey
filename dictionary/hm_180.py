#字典,键值对

xiaoming = {"name" : "Xiaoming",
            "age" : 18,
            "gender" : "Male",
            "weight" : 70,
            "height" : 180}
print(type(xiaoming))
print(xiaoming["name"])
#取值的时候，如果键不存在，会报错

#增加key和value

xiaoming["score"] = 99.7
print(xiaoming)

#改值
xiaoming["score"] = 99
print(xiaoming)

#删除，用pop，如果删除的key不存在，会error
xiaoming.pop("gender")
print(xiaoming)

#用for遍历所有的key和value
for k in xiaoming:
    print(f"{k} is {xiaoming[k]}")

