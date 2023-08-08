'''Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30. '''
l = list()
for i in range(1,21):
	l.append(i**2)
print(l[:5])#Squres of first 5 (1,2,3,4,5)
print(l[-5:])#Squres of last 5 (20,19,18,17,16)


