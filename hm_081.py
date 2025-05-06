"""
import keyword
print(keyword.kwlist)
"""

#the rule of the name for varies
# if combine with two words, require two of the word is lower, connect together by using "_"

#the other way is Camel Case which is the first word lower, the second word upper, for example:"firstWord","FirstWord"

"""
if rule, use 4 times space instead of the Tab
"""

"""
age = int(input("age: "))
if age >= 18:
    Tab = "Approved to enter this place"
elif age <= 18 or age >= 60 :
    Tab = "Not approved to enter this place"
print(Tab)
"""

"""
== equal to 
!= unequal to 
> more than
< less than
>= more than or equal to
<= less than or equal to 

age = int(input("age: "))
if age >= 18:
    if_student = input("Is student ? (Y/N) ")
    if if_student == "N":
        Tab = "Approved to enter this place"
    else:
        Tab = "Not approved to enter this place"
print(Tab)

age = int(input("age: "))
if  18 <= age <= 60:
    Tab = "Approved to enter this place"
elif age >60:
    Tab = "Not approved to enter this place"
elif input("is student ? (Y/N) ") == "N":
    Tab = "Approved to enter this place"
else:
    Tab = "Not approved to enter this place"
print(Tab)


# "or" "and" practices
python_score = int(input("Python score: "))
c_score = int(input("C score: "))

if python_score >=60 or c_score >=60:
    Tab = "You have pass the test"
else:
    Tab = "You have not pass the test"
print(Tab)


# Boolean practices
varify = input("Is employer in this company? (Y/N) ")
if varify == "N":
    varify_result = 0
else:
    varify_result = 1
if not varify_result:
    print("Not employer in this company")
else:
    print("Employer in this company")

# if elif practices by using scenario of girlfriend present.
holiday = input("Please input the option of Holiday (A/B/C): ")

if holiday == "A":
    print("Buy apple")
elif holiday == "B":
    print("Buy bear")
elif holiday == "C":
    print("Buy strawberry")
else:
    print("everything is ok!")
"""
#Check passenger's ticket and
#check the ticket for passenger
check_ticket = input("Input the result of ticket-checking (Y/N): ").strip().upper()
check_packages = ""
if check_ticket == "Y":
    check_packages =  input("Input the result of packages-checking (Y/N): ").strip().upper()
    if check_packages == "Y":
        print("Keep going!")
    else:
        print("Go back!")
else:
    print("Go back!")