#Write a Python program to remove duplicates from a list.
l1=[1,11,1,1,1,1,5,5,5,4,5,4,5,6,8,8,6,6,6]
unique_list=[]
for i in l1:
    if i not in unique_list:
        unique_list.append(i)
    else:
        pass
dup=unique_list
print(dup)
