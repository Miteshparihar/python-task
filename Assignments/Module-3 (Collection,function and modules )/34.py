'''Write a Python script to check if a given key already exists in a
dictionary. '''
dic = {'a': 100, 'b':200, 'c':300}
key = 'a'
if key in dic.keys():
    print("Present, ", end =" ")
    print("value =", dic[key])
else:
        print("Not present")    

