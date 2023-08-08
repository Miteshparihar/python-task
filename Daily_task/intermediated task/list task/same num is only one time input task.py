'''take 10 elements from user & find the unique elements from list 
l1=[12,23,34,23,54,67,34,12,34,66]
unique_list=[12,23,34,54,67,66]'''
lis=[45,45,124,544848,45,78,12,12,12,88,88,9,10]
unique=[]
for i in lis:
    if i not in unique:
        unique.append(i)
    else:
        pass
print(unique)
