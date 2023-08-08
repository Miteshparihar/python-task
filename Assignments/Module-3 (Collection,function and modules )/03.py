#Differentiate between append () and extend () methods?
'''     append()                                                                 extend()
> This is used for add new list in other list   > This is used for add element in other list
    (nested list)                                               
'''
#append()              
lst_1=[4544,55,8,2,8,2,555,4]
lst_2=['mitesh','Ansh']
lst_1.append(lst_2)
print(lst_1)
#extend()
lst_1=[4544,55,8,2,8,2,555,4]
lst_2=['mitesh','Ansh']
lst_1.extend(lst_2)
print(lst_1)
