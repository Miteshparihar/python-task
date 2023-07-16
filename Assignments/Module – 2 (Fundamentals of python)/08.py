'''Write a Python program to test whether a passed letter is a vowel or
not. '''
user = input("Input a letter of the alphabet: ")

if user in ('a', 'e', 'i', 'o', 'u'):
	print("This is a vowel",user)
else:
	print("This is a not vowel",user) 
