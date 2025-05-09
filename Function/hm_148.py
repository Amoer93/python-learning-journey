def test_1():
    print("*" * 20)

def test_2():
    print("-" * 20)

def test_3():
    '''
    Nested Function Call
    '''
    test_1()
    test_2()
    test_1()

test_3()