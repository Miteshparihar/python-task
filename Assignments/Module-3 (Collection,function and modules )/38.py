#Write a Python program to check multiple keys exists in a dictionary
sports = {"geeksforgeeks" : 1, "practice" : 2, "contribute" :3}
print(sports.keys() >= {"geeksforgeeks", "om"})
print(sports.keys()>={"contribute", "practice","geeksforgeeks"})
