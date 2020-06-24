#TASK 2

#Program for 7 different methods of tuples

#Initializing the tuples
myTup = ('football', 'cricket', 'badminton')
tuple = (23, 25, 32, 52, 45, 54)

#Legnth of a tuple
print("Legnth of the tuple is: ", len(myTup))

#Slicing of a Tuple
myTup[0:2]
print("The updated tuple: ", myTup[0:2])

#Deleting a tup
del tuple

#Printing elemnets with the max value
print("The max value element is: ", max(myTup))

#Printing elemnets with the min value
print("The max value element is: ", min(myTup))

Tuple in reverse order
myTup[::-1]
print("The tuple in the reverse order is: ", myTup[::-1])
