#TASK-4
#Question 2 (a)

#Function for square of a number
def squarefunc():
    z=int(input("Enter the number, of which you want to calculate the square: "))
    sq = z*z
    print("\nThe square of the number is: ", sq)

#Function for min and max number in a list

def minAndMaxFunc():
#For minimum
    minNum = createList[0] 
    for i in createList:
        if(minNum > i):
            minNum = i
    
#For maximum
    maxNum = createList[0] 
    for i in createList:
        if(maxNum < i):
            maxNum = i
    
#Function for finding the sum of all elements in the list
def sumfunc():
    sum = 0
    for x in range(0, l):
        sum = sum + createList[x]

