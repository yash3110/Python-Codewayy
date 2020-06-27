#TASK-4
#QUESTION-2 (b)

#Program to find the middle char, count the number of vowels, calculate the legnth and the number of words in a string
    
#For Middle Char
def midChar():
    if(len(str) % 2 == 0):
        print(str[(int(len(str) / 2) - 1 )] + " " +"and" + " " + str[(int(len(str) / 2))])
    else:
        print(str[(int(len(str)/2))])

#To find the vowel in the string
def calVowel():
    vowels=0
    for char in str:
        if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
            vowels = vowels + 1
           
#To calculate number of letters in the string 
def calLetters()
    letters = 0    
    for i in str: 
        letters += 1

