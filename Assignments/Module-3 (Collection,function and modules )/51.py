#Write a Python function that checks whether a passed string is palindrome or not

def pali(string):
    if(string==string[::-1]):
        return "The string is palindrome."
    else:
        return "The string is  not plalindrome"
string=input("Enter string:-")
print(pali(string))
