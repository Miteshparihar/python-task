'''Write a Python function that takes two lists and returns true if they have
at least one common member. '''
list_1=[1,2,3,4,5,6]
list_2=[6,7,8,9,10,11]
result=False
for i in list_1:
    for j in list_2:
        if i==j:
            result=True
print(result)
