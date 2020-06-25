#TASK-3

# 3) A program using for loop that prints all numbers from 1-10 except 3 and 7

for var in range(1, 11):
    if (var == 3 or var == 7):
        continue
    print(var, end='')
    print("\n")

# A program using for loop that prints all numbers from 1-10 except 3 and 7
print("\n")
print("\n")
num=1
while(num!=11):
    if(num == 3 or num == 7):
        num+=1
    else:
        print(num)
        num+=1
    print("\n")
