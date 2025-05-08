def Multiplication_Table(numbers):
    print("This is a 9 * 9 \"Multiplication Table\"")
    row_1 = 1
    col_1 = 1
    while row_1 <= numbers:
        col_1 = 1
        print(f"{col_1} * {col_1} = {col_1 * col_1}",end = "\t")
        while col_1 < row_1:
            print(f"{col_1} * {row_1} = {col_1 * row_1}",end = "\t")
            col_1 += 1
        print("")
        row_1 += 1
Multiplication_Table(3)