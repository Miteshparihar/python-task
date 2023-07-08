#task To get user input and find even or odd 
even=0
odd=0
for user in range(5):
      get=int(input("enter number:- "))
      if get%2==0:
            even+=1
      else:
            odd+=1
print("even:-",even)
print("odd:-",odd)
