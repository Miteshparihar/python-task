#Write a Python program to map two lists into a dictionary
fruits = ['mango', 'pear', 'apple','papaya']
price = [55, 78, 110, 60]

fruits_price = zip(fruits, price)

fruits_dict = {}

for key, value in fruits_price:
    if key in fruits_dict:
        pass 
    else:
        fruits_dict[key] = value
        
print(fruits_dict)
