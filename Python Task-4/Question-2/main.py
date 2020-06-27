import lists
import operators
import strings

#Using lists functions
lists.squareFunc(z)

#Taking input from the user
#Initializing the list
createList = []

#Taking input for the list
l = int(input("\nEnter the number of elements you want to include in the list: "))
print("\nEnter the elements: ")
for nums in range(l):
    elements=int(input())
    createList.append(elements)
print("Your list is: ", createList)

lists.minAndMaxFunc(createList)
print("\nThe minimum element is: ", minNum)
print("The maximum element is:", maxNum)

lists.sumFunc(createList)
print("The sum of all elements of the list is: ", sum)   


#Using string functions
#Taking input from the user
str = input("\nEnter the Word: ")
#To Find the middle character
strings.midChar(str)
#To find the vowel in the string
strings.calVowels(str)
print("Number of vowels vowels are:",)
#To calculate number of letters in the string 
strings.calLetters(str)
print("The number of letters are: ", letters)


#Using Operator functions
#Taking input from the user
a=int(input("\nEnter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
operators.andOper(a,b,c)
operators.orOper(a,b,c)
operators.notOper(a)

    

