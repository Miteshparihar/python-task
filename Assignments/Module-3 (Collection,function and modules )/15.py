#Write a Python program to get unique values from a list
list_1=[1,11,2,11,2,44,5,4,5,4,1,1,1,25]
blank=[]
for i in list_1:
    if i not in blank:
        blank.append(i)
print(blank)
