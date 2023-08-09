#string task
#task-1 (find length)
st="Mitesh     mali"
print(len(st))



#task - 2(find character)
hel="fjhdgiu efeufeufgueuiehy"
print(hel.count("u"))



#task-3 (count each character)
string = "Hello good morning"
all_char ={ }
print(type(all_char))
for i in string:
    if i in all_char:
        all_char[i] += 1
    else:
        all_char[i] = 1

print("Count of all characters in Hello good morning is :",all_char)




'''task : 4

take user input as string : Hello Friends I have 5 Chocolates

Total Voewls : 
Total Consonants : 
Total Digits : 
Total White Spaces : '''
#vowels or consonent
user=input("Please enter a string as you wish: ");
vowels=0
consonants=0
for i in user:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
             vowels=vowels+1;
    else:
            consonants=consonants+1;
print("The number of vowels:",vowels);
print("The number of consonant:",consonants);
#white space
string= input("Check white space:-")
count=0
for i in range(0,len(string)):
    if string[i]==" ":
        count+=1
print(count)

#digit count






