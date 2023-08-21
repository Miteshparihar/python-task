#File read
# r : open file to read data from  it
'''
file.read()
file.readline()
file.readlines()
'''
file = open ("My_first.txt",'r')
print(file.readlines())
file.close()
