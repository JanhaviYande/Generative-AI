# Write a program to check if entered number is a palindrome or
# not.
def palindrome(n):
    rev = 0
    temp = n
    while n != 0:
        d = n%10
        rev = (rev*10)+d
        n //= 10

    if temp == rev:
        return True
    else:
        return False

num = int(input("Enter a number : "))
if palindrome(num):
    print(num,"is palindrome") 
else:
    print(num,"is not palindrome")   