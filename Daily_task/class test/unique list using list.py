#take list of 10 numbers from user & find unique list from it.
lst=[ ]
user=int(input("how many element:-"))
for i in range(0,user):
    user_1= int(input("list:-"))
    lst.append(user_1)
print(lst)
m=list(set(lst))
print(m)
