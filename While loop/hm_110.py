
'''
# print "hello python" 5 times
i = 1 # def varify
n = 0
while i < 6:
    print("hello python")
    print(f"This is {i} time")
    i = i + 1 # add the number of time
    n = n + 1
print(f"The final result is {n}")
# +=  -=
a = 1
a += 1
c = 1
c = c + 1
print( c == a)
'''

# python indexing starting from 0

#calculate the summary from 0 to 100, without even
i = 0
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1

print(sum)




