'''Write a Python function to insert a string in the middle of a string. '''
def insert_sting(str, word):
	return str[:2] + word + str[2:]

print(insert_sting('[{}]', 'Python'))
