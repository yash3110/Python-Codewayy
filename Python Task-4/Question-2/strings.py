#TASK-4
#QUESTION-2 (b)

#Program to find the middle char, count the number of vowels, calculate the legnth and the number of words in a string


def stringFunc():
    str = input("\nEnter the Word: ")
    
#For Middle Char
    if(len(str) % 2 == 0):
        print(str[(int(len(str) / 2) - 1 )] + " " +"and" + " " + str[(int(len(str) / 2))])
    else:
        print(str[(int(len(str)/2))])

#To find the vowel in the string
    vowels=0
    for char in str:
        if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
            vowels = vowels + 1
    print("Number of vowels are:", vowels)
           
#To calculate number of letters in the string    
    letters = 0    
    for i in str: 
        letters += 1
    print("The number of letters are: ", letters)



