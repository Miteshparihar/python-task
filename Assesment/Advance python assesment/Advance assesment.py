# >>>>>>>>>>>>>>>>>>>>>>>>>>Advance Assesment
import mysql.connector

#>>>>>>>>>>>>>>>>>>>>>>>>>>>database connectivity
def connection():

    return mysql.connector.connect(
        user="root",
        host="localhost",
        password="",
        database="pharmacy")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>class creation
class Admin:
    def register(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>Register")
        self.admin_name=input("Enter your name :- ")
        self.admin_password=input("Enter password:-")
        print(">>>>>>>>>>>>>>>>>>Admin registraton done >>>>>>>>>>>>>>>>>")
    def login(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>> Login")
        self.admin_name1=input("your name :- ")
        self.admin_password1=input("your password:-")
        if self.admin_name==self.admin_name1 and self.admin_password==self.admin_password1:
            print(">>>>>>>>>>>>>>>>>>> Admin login Success >>>>>>>>>>>>>>>>>>")
        else:
            print("Error:- Password or name not match !!!!")
    def view_manager(self):
        vman=input("You want to view all manager list(y/n):-")
        if vman=="y" or vman=="Y":
            con=connection()
            cursor=con.cursor()
            query = "select * from manager " 
            cursor.execute(query)
            row=cursor.fetchall()
            print("All Manager Data  :- ",row)
            con.commit()
            con.close()
    def view_medicine(self):
        vmed= input("You want to view all medicine (y/n):- ")
        if vmed=="y" or vmed=="Y":
            con=connection()
            cursor=con.cursor()
            query = "select * from medicine " 
            cursor.execute(query)
            row=cursor.fetchall()
            print("All medicine Data  :- ",row)
            con.commit()
            con.close()
        else:
            print(" >>>>>>>>>>>>>>>>>>>>>>>>Thanks >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
class Pharmacy_manager:
    def register(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>Register")
        self.name=input("Enter your name :- ")
        self.password=input("Enter password:-")
        self.shop=input("Enter pharmacy_shop name :-")
        print("Your registraton done >>>>>>>>>>>>>>>>>")
    def login(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>> Login")
        self.name1=input("your name :- ")
        self.password1=input("your password:-")
        self.shopname=input("Shop name:- ")
        if self.name==self.name1 and self.password==self.password1:
            con=connection()        
            cursor=con.cursor()
            query="insert into manager(Name,Shop) values(%s,%s)"
            args=(self.name1,self.shopname)
            cursor.execute(query,args)
            con.commit()
            con.close()
            print("Your Data stored success>>>>>>>>>>>>>>>>>>>>")
            table_name='manager'
            user=input("check manager_name and shop_name (y/n):-")
            if user=='y' or user=='Y':
                con=connection()
                cursor=con.cursor()
                query = "select * from manager where Name=%s" 
                args=(self.name1,)
                cursor.execute(query,args)
                row=cursor.fetchall()
                print("Manager Data  :- ",row)
                con.commit()
                con.close()
        else:
            print("name or password not match !!!")     
    def add_medicine(self):
        medi=input("You want to add medicine in medicine table(y/n):-")
        if medi=="y" or medi=="Y":
            self.mediname=input("Enter medicine name :- ")
            self.Qty=int(input("Enter Qty:-"))
            self.Date=input("Current Date :-")
            self.Add=input("Added by :-")
            self.Price=int(input("Price:-"))
            con=connection()        
            cursor=con.cursor()
            query="insert into medicine(Medicine_name,Qty,Date,Add_by,Price) values(%s,%s,%s,%s,%s)"
            args=(self.mediname,self.Qty,self.Date,self.Add,self.Price)
            cursor.execute(query,args)
            con.commit()
            con.close()
            print(" >>>>>>>>>>>>>>>>>>>>>>>>Add medicine Successfull>>>>>>>>>>>>>>>>>>>>>>>>>")
            
    def view_medicine(self):
        medi_view=input("you want to view medicine data(y/n):-")
        if medi_view=="y" or medi_view=="Y":
            self.your_medi=input("Your medicine name :- ")
            self.your_Add=input("Who added :-")
            con=connection()
            cursor=con.cursor()
            query = "select * from medicine where Medicine_name=%s" 
            args=(self.your_medi,)
            cursor.execute(query,args)
            row=cursor.fetchall()
            print("Your medicine table :- ",row)
            con.commit()
            con.close()
    def delete_medicine(self):
        self.medi_delete=input("You want to delete medicine (y/n):-")
        if self.medi_delete=="y" or self.medi_delete=="Y":
            de_medi=input("Enter medicine name and delete :-")
            con=connection()
            cursor=con.cursor()
            query="delete from medicine where Medicine_name=%s"
            args=(de_medi, )
            cursor.execute(query, args)
            con.commit()
            con.close()
            print("Delete Success >>>>>>>>>>>>>>>>>>>>>>>")
        else:
            print(">>>>>>>>>>>>Thanks>>>>>>>>>>>>>>>>>>")
#>>>>>>>>>>>>>>>>>>>>>>>>>>
menu='''
        >>>>>>>>Select usertype >>>>>>>>>>
                       1.Admin
                       2.Pharmacy_manager
'''
print(menu)
choice=input("Enter your choice :- ")
if choice=='1':
    ad=Admin()
    ad.register()
    ad.login()
    ad.view_manager()
    ad.view_medicine()
        
elif choice=='2':
    pmanager=Pharmacy_manager()
    pmanager.register()
    pmanager.login()
    pmanager.add_medicine()
    pmanager.view_medicine()
    pmanager.delete_medicine()
else:
    print("Incorrect select valid !!!")

