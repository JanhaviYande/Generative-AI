# Write a program to print first n prime numbers

n = int(input("Enter value for n : "))

for num in range (2,n+1):
    isprime = True
    for i in range (2,num):
        if num%i == 0:
            isprime = False
            break
    if isprime:
        print(num)             
