# Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms
def fibonacci(n):
    a,b = 0,1
    while a <= n:
        print(a,end=" ")
        a,b = b, a+b
       
    
num = int(input("Enter a number : "))
fibonacci(num)