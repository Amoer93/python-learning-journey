'''
# print end
row = 1
while row <= 5:
    stars = "*" * row
    print(stars,end= " ")
    row += 1

row_1 = 1
while row_1 <= 5:
    stars_1 = "*" * row_1
    print(stars_1)
    row_1 += 1
'''
row_1 = 1
col_1 = 1
while row_1 <= 5:
    col_1 = 1
    print("*",end = "")
    while col_1 < row_1:
        print("*",end = "")
        col_1 += 1
    print("")
    row_1 += 1