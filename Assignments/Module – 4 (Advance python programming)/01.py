#What is File function in python? What is keywords to create and write file. 
'''
Ans:- python file object provide methods  and attributes to access and manipulate files.using file object,we can read
           and write any files.
'''
#Keyword to create file
'''x : to create a file
  w : to write into file & create a file  write will override the previous content of the file 
    it will replace new content with old content'''
#File create
'''create=open("basic.txt","x")
create.close()'''
#write in basic.txt
file=open("basic.txt","w")
file.write("Hello good morning")
file.close()
