#TASK-4
#QUESTION-2 (c)

#Use of all logical operators

a=int(input("\nEnter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))

#And operator
def andOper(a,b,c):
    if a == b and b==c and a ==c:
        print("\n All the three numbers are equal")
    if b == a and b == c:
        print(" \n a is equal to c ")
    elif a == c and a == b:
        print(" \n b is equal to c ")
    elif c == a and c == b:
        print(" \n a is equal to b ")
    else:
        print(" \n The three numbers are not equal ")

andOper(a,b,c)

#Or operator       
def orOper(a,b,c):
    if a > c or b > c: 
        print("\nc is not the largest number")
    else:
        print("\nc is the largest number")
        
    if a > b or c > b:
        print("\nb is the not the largest number")
    else:
        print("\nb is the largest number")

    if b > a or c > a:
        print("\na is the not the largest number")
    else:
        print("\na is the largest number")

orOper(a,b,c)

#Not operator        
def notOper(a): 
    if not a > 0:
        print(" \n a is a negative number ")
    else:
        print(" \n a is a positive number ")

notOper(a)
