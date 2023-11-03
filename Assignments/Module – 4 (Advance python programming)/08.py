#Write a python program to find the longest words. 
sentence = input("Enter sentence: ")
longest = max(sentence.split(), key=len)
print("Longest word is: ", longest)
print("length is: ", len(longest))
