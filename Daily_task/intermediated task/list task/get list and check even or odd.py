#task : 1 take a number list,ex:-num_list=[12,34,15,67,43]
num=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
