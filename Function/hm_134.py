def Multiplication_Table(input_number = None):
    '''
    :param input_number:
    :return:
    '''
    input_number = int(input("Please enter the numbers you wish to multiply: "))
    print(f"This is a {input_number} * {input_number} \"Multiplication Table\"")
    row_1 = 1
    col_1 = 1
    while row_1 <= input_number:
        col_1 = 1
        print(f"{col_1} * {col_1} = {col_1 * col_1}",end = "\t")
        while col_1 < row_1:
            print(f"{col_1} * {row_1} = {col_1 * row_1}",end = "\t")
            col_1 += 1
        print("")
        row_1 += 1

def Say_hello(input_number = None):
    '''
    :param input_number:
    :return:
    '''
    times_hello = 0
    helloed_times_number = 0
    input_number = int(input("please enter a number: "))
    while times_hello < input_number:
        print("Hello World")
        helloed_times_number += 1
        print(f"This is the {helloed_times_number} times say hello")
        times_hello += 1

def add_print(num1, num2): # num1, num2 are parameter
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")

def add_return(num1, num2):
    '''
    对函数结果进行返回，但是需要使用变量接受计算结果
    '''# num1, num2 are parameter
    result = num1 + num2
    return result
    result_2 = num1 * num2 # after return, code will be missing
