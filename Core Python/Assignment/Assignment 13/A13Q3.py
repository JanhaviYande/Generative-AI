# Python Program to Check if a Given Key Exists in a Dictionary or Not
my_dict = {1:"Janhavi",2:"Shreya",3:"Aditya",4:"Atharva"}
key = int(input("Enter a key to be searched : "))
if key in my_dict:
    print("Key exists")
else:
    print("Key does not exists")