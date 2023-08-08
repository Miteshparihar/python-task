# enter email and login this same email or password
print('welcome to Registration process')
email=input("e-mail:-")
p1=input("password:-")
dic={ }
if len(p1)>=4 and len(p1)<=8:
    dic={'email': email,'password':p1}
    print(dic)
    print("Registration succesfully")
    print("Login page")
    e1=input("e-mail:-")
    p2=input("password:-")
    if e1==email and p2==p1:
        print("Succesfully Login")
    else:
        print("Failed")
else:
    print('Please enter password min- 4 or max-8')
    
