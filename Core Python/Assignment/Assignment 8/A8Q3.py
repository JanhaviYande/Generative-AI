# Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum(n):
    s = 0
    for i in range(1,n+1):
        s += i 
    return s

def sum_fact(n):
    fact = 1
    s = 0
    for i in range(1,n+1):
        fact *= i
        s += fact
    return s    

def sum_power(n):
    s = 0
    for i in range(1,n+1):
        s += i ** i
    return s

    
num = int(input("Enter a number : "))
print("sum = ",sum(num))
print("sum of factorial = ",sum_fact(num))
print("sum of power = ",sum_power(num))
