'''
i = 0
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
    if sum > 250:
        break
print(sum)
'''
#calculate the summary from 0 to 100, without even, and stop when the sum above 250

#calculate the summary from 0 to 100, and skip when i = 50
i = 0
sum = 0
while i <= 100:
    if  i == 50:
        i = i + 1
        continue
    sum = sum + i
    i = i + 1
print(sum)
