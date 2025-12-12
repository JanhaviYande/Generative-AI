# Sum of all odd numbers between 1 to n
def sum_of_odd(n):
    sum = 0
    for i in range(1,n+1):
        if i % 2 != 0:
            sum += i
    return sum
    
num = int(input("Enter a number : "))
print("Sum of odd numbers = ",sum_of_odd(num))    

