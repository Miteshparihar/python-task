'''Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings. '''
lst=["mademm","3643","apple","3756","33"]
count = 0
for x in lst:
	if len(x) >= 2 and x[0] == x[-1]:
	   count+= 1
print(count)
