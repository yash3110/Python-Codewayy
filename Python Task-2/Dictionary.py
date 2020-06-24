#TASK 2

#Program for 7 different methods of dictionary

#Initialize the dictionary
voc = ('Name': 'Yash', 'Age': 19 'Course': 'B-Tech CSE')
print (voc)

#Printing elemnts using key
print("Name: ", voc['Name'])

#Add a new key
voc['college'] = "Amity University"
print (voc)

#Printing (keys,values) pair of dictionary items
voc.item()
print("key, value pair of dictionary: ", voc.items())

#Remove Entry using key
del voc['Course']
print(voc)

#legnth of a dictionary
print ("legnth of the dictionary is: ", len(voc))
