 # Task -- user input any and get year , month , days .
 #year 
year = int(input("enter year:- "))
print("year is :- " ,year)

months = 12*year
print("Month is :- ",months)

days = 30*months
print("days is :- ",days)

#months
months = int(input("enter months:-"))
print("months:-",months)

year =months//12
print("year:- ",year)

days = 30*months
print("days:- ",days)

#days
days = int(input("enter days:-"))
print("days:-",days)

months= days/30
print("months:-",months)

year =days/360
print("year:-",year)




