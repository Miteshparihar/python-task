#Write a Python program to read last n lines of a file. 
a_file = open("basic.txt", "r")
lines = a_file.readlines()
last_lines = lines[-5:]
print(last_lines)
a_file.close()
