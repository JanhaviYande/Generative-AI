# Python Program to Remove the Given Key from a Dictionary
my_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
key = int(input("Enter key to be removed : "))
my_dict.pop(key)
print(my_dict)