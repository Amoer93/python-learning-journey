name_list = ["Jam","Porter","Peter"] #input data into list
print(name_list) #show the list

print(name_list[1]) #output the second data

name_list.append("Jack")
print(name_list) #show the list

# the maximem
#print(name_list[4])

#find data's index
# print(name_list.index("Jam"))
# print(name_list.index("Jam1")) # if the data which is input does not belong to the list, will be error

#change data
name_list[1] = "Harry"
print(name_list[1])
name_list.insert(1,"Honey")
print(name_list[1])

temp_list = ["Zhangsan","Lisi","Wangwu"]
name_list.extend(temp_list) #extend can adding other list into the end of this list
print(name_list)

temp_list.remove("Wangwu") # remove method
print(temp_list)
temp_list.pop(0) # pop method
print(temp_list)

name_list.pop()
print(name_list)

temp_list.clear()
print(temp_list)

del name_list[1]
print(name_list)

print(f"the list contain {len(name_list)} items") # len can calculate the count of the list