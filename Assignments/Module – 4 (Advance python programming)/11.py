# 11 Write a Python program to write a list to a file
items = ['Table ', 'Chair ', 'Mirror ', 'Curtain ', 'Almirah ']
file = open('items.txt','w')
file.writelines(items)
file.close()
