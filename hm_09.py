# my name is Xiaoming

name = input("What is your name? ")

print("Hello, " + name + "!")
print("Hello, %s!" % name)
print(f"Hello, {name}!")

#student number is 000001
student_no = input("What is your student number? ")
print("Hello, %s, Your number is %06d!" % (name, int(student_no)))
#the %06d means if the length shorter than 6, then complement automatically, otherwise use the initial input