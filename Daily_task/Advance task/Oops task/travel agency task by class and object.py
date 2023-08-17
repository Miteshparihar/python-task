class C1:
    print('''
              =========Welcome to travel ==========
              1. NY
              2. America
              3. France
              4. England
              5. india
              6. Germany
              7. Australia
              8. japan
              9. nepal
              10.peru
              ''')
    user=input("Do you want membership ? ['y/n'] : ")
    if user=='y' or user=='yes':
        print("Then follow registration process")
    else:
        print("Thank you")
class C2:
        print('''
    ===============Welcome to registration process============
    ''')
        def __init__(self):
            status =True
            while status:
                self.email=input("Enter email :")
                self.password=input("Enter password :")
                self.con_password=input("Enter confirm password :")
                if self.password==self.con_password:
                    print("Registration completed.....")
                    status=False
                else:
                    print("Error !!")
                    status=True
ob=C2()
class C3:
    print('''
             =================Login To Account===========
''')
    def __init__(self):
        self.email_log=input("Enter email : ")
        self.password_log=input("Enter password:")
obj1=C3()
if obj1.email_log==ob.email and obj1.password_log==ob.password:
            print("Login success")
else:
            print("Access Denied !!!")
    
        
