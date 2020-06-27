#TASK-4
#Question 2 (a)

#Function for square of a number
def squarefunc():
    z=int(input("Enter the number, of which you want to calculate the square: "))
    sq = z*z
    print("\nThe square of the number is: ", sq)

#Initializing the list
createList = []

#Taking input for the list
l = int(input("\nEnter the number of elements you want to include in the list: "))
print("\nEnter the elements: ")
for nums in range(l):
    elements=int(input())
    createList.append(elements)
print("Your list is: ", createList)

#Function for min and max number in a list

def minAndMaxFunc():
#For minimum
    minNum = createList[0] 
    for i in createList:
        if(minNum > i):
            minNum = i
    print("\nThe minimum element is: ", minNum)

#For maximum
    maxNum = createList[0] 
    for i in createList:
        if(maxNum < i):
            maxNum = i
    print("The maximum element is:", maxNum)
    
#Function for finding the sum of all elements in the list
def sumfunc():
    sum = 0
    for x in range(0, l):
        sum = sum + createList[x]
    print("The sum of all elements of the list is: ", sum)
    
    

