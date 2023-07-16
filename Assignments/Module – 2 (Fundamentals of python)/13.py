''' Write a Python program to count the number of characters (character
frequency) in a string '''
user=input("Enter a string:- ")
blank={}
for i in user:
    if i in blank:
        blank[i]+=1
    else:
        blank[i]=1
print(blank)

