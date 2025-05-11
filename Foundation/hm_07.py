#069
"""
收银员输入苹果价格，单位：元/斤
收银员输入苹果数量，单位：斤
"""
# input the price of apples
price_apple = input("<price of apples>: ")
# input the weight of apples
weight_apple = input("<weight of apples>: ")
# calculate the total price of apples
money_apple = float(price_apple) * float(weight_apple)
print(f"the total price of apple is {money_apple}")

print("%0.2f" % money_apple) # adding the format in the result
print(f"{money_apple:,.2f}")
