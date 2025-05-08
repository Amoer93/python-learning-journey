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
while row_1 <= 9:
    col_1 = 1
    print(f"{col_1} * {col_1} = {col_1 * col_1}",end = " ")
    while col_1 < row_1:
        print(f"{col_1} * {row_1} = {col_1 * row_1}",end = " ")
        col_1 += 1
    print("")
    row_1 += 1

#\t, \n, can be using in different situation, and can using \ to Escape character
print("This is a 9 * 9 \"Multiplication Table\"")
row_1 = 1
col_1 = 1
while row_1 <= 9:
    col_1 = 1
    print(f"{col_1} * {col_1} = {col_1 * col_1}",end = "\t")
    while col_1 < row_1:
        print(f"{col_1} * {row_1} = {col_1 * row_1}",end = "\t")
        col_1 += 1
    print("")
    row_1 += 1