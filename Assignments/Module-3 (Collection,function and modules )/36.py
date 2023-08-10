#How Do You Check The Presence Of A Key In A Dictionary?
dic = {'a': 100, 'b':200, 'c':300}
 
# check if "b" is none or not.
if dic.get('d') == None:
  print("Not Present")
else:
  print("Present")
