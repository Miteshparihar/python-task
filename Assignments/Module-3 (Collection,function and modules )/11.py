'''Write a Python function that takes a list and returns a new list with unique
elements of the first list. '''
lst_1=[1,1,1,2,2,4,5,7,5]
blank=[]
for i in lst_1:
    if i not in blank:
        blank.append(i)
    else:
        pass
print(list(blank))

