# using of class and object take input from user and display accordingly
class Cls():
    def input(self):
        self.name=input("Enter Name :")
        self.age=input("Enter Age : ")
        self.gender=input("Enter gender :")
        self.email=input("Enter E-mail :")
        self.address=input("Enter Address :")
    def displey(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("gender :",self.gender)
        print("E-mail :",self.email)
        print("Address :",self.address)
obj=Cls()
obj.input()
print("==========your Info=========")
obj.displey()
