#TASK-4
#Question-1

#Taking matrix input from user
n = int(input("Enter the number of elements for the matrix: "))
        
#Creating the matrix
theMat = [list(range(1+n*i, 1+n*(i+1)))
          for i in range(n)]

print("\nYour Matrix is:\n ", (theMat))

#A new matrix is defined for single list
matNew = [] 

#The matrix is converted into a single list
for i in theMat: 
    for j in i: 
        matNew.append(j)
print(matNew)

#Prime Numbers in the created matrix
print("\nThe prime Numbers in the matrix are: ")
for x in matNew:
    if(x>1):
        for j in range(2, x):
            if(x%j == 0):
                break
        else:
            print(x)
        

