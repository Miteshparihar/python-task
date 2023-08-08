#Write a Python program to convert a list of tuples into a dictionary.
#first method
'''def conv(tup,dic): #function define 
    dic=dict(tup) #convert tuple to dict and stored dic variable     
    return dic 
tup = [("Raja", 10), ("kuldeep", 12), ("Mitesh", 14),("mritunjay", 20), ("Ansh", 25), ("piyush", 30)]
dics={}
print(conv(tup,dics))'''
#secand method 
tup = [("Raja", 10), ("kuldeep", 12), ("Mitesh", 14),("mritunjay", 20), ("Ansh", 25), ("piyush", 30)]
dics={}
dic = dict(tup)
print(dic)
