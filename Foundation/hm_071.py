# my name is Xiaoming
"""

name = input("What is your name? ")

print("Hello, " + name + "!")
print("Hello, %s!" % name)
print(f"Hello, {name}!")

#student number is 000001
student_no = input("What is your student number? ")
print("Hello, %s, Your number is %06d!" % (name, int(student_no)))
#the %06d means if the length shorter than 6, then complement automatically, otherwise use the initial input

# input the price of apples
price_apple = input("<price of apples>: ")
# input the weight of apples
weight_apple = input("<weight of apples>: ")
# calculate the total price of apples
money_apple = float(price_apple) * float(weight_apple)
print(f"the total price of apple is {money_apple}")

print("%0.2f" % money_apple) # adding the format in the result
print("The price of apple is %.2f, the weight is %.02f, you need to pay %.02f" % (float(price_apple), float(weight_apple),float(money_apple)))


"""
#scale, output 10.00%
scale = 0.25
print("the property of number is %.2f%%" % (scale*100))