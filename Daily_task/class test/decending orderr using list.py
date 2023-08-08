#take a list of 10 numbers from user & sort the list in decsending order (using inbuilt function)
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)  
print(lst)
lst.sort(reverse=True)
print(lst)

