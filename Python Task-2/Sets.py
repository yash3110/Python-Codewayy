#TASK 2

#Program for 7 different methods of sets

#Initializing the set
set-1 = {1, 3, 5, 7, 3, 6, 9, 13, 17}
set-2 = {2, 4, 6, 8, 10, 3, 11, 19, 17}

#Printing the set
print (set-1)

#Union of 2 sets
set-3 = set-1.union(set-2)
print ("The union of the two sets is: ", set-3)

#Intersection of two sets
set-3 = set-1.intersection(set-2)
print ("The intersection of two sets is: ", set-3)

#Adding element to a set
set-1.add(35)
print ("The first set after adding the element: ", set-1)

#Removing an element from a set
set-1.discard(13)
print ("New set: ", set-1)

#Symmetric difference between two sets
set-3 = set-1.symmetric_difference(set-2)
print ("The symmetric difference in the two sets: ", set-3)

#Removing duplicates from lists using sets
list-1 = [1, 2, 4, 16, 2, 17, 22, 17, 23]
list-2 = set(list-1)
list-2 = list(set(list-1))
print("The list withour repition of numbers is: ", list-2)
