# Write a program to find sum of digits of a number.
def sum_of_digit(n):
    sum = 0
    while n>0:
        d = n% 10
        sum += d
        n //= 10
    return sum

num = int(input("Enter a number : "))  
print("Sum of digit = ",sum_of_digit(num))  