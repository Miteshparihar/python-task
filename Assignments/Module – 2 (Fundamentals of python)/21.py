'''Write a Python function to reverses a string if its length is a multiple of
4.'''
string=input("Enter the String :")
if len(string) % 4 == 0:
   print(''.join(reversed(string)))
else:
	print(string)
