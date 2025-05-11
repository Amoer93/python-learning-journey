def print_line():
    print("-" * 50)

def print_line1(num):
    print("-" * num)

def print_line2(char,num):
    print(char * num)

def print_line3(time):
    times = 0
    while times < time:
        print_line()
        times += 1

# print_line3(5)

def print_line4(char,num,time):
    """
    print mult line
    :param char: line's char
    :param num: single lins char's number
    :param time: line's time
    """
    times = 0
    while times < time:
        print_line2(char,num)
        times += 1
# print_line4("+",10,3)
