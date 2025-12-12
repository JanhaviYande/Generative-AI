# Write a program to check if entered year is a leap year or not.
def leap_year(year):
    if (year % 400 == 0)or (year % 4 and year % 100 != 0):
        return True
    else:
        return False
    
year = int(input("Enter a year : "))
if leap_year(year):
    print(year,"is a leap year")  
else:
    print(year,"is not a leap year")     