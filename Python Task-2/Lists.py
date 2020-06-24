#TASK - 2

#Program for 7 different methods of lists

#To initialize the list
random = [5, 7, 29, 37, 18]

#To print this list
print ("The list of these random numbers: ", random)

#The index of the elements
random.index(37)
print ("The index of the element 37 is: ", random.index(37))

#To Change the element at a particular index
random[4] = 10
print ("The updated list is: ", random)

#Sorting the list
random.sort()
print ("The sorted list is: ", random)

#To add elements in the list
random.append(33)
print ("The list after adding the element at the end of the list: ", random)

#Remove elements from a list
random[0:2] = []
print ("The list after removing the elements: ", random)
