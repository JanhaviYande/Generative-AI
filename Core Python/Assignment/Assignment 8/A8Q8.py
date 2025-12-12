# Write a program find reverse of a number
def reverse(n):
    rev = 0
    while n>0:
        d = n%10
        rev = rev*10 + d
        n //= 10
    return rev

num = int(input("Enter a number : "))
print("Reversed number = ",reverse(num))    
    