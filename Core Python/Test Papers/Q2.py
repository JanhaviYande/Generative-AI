#Write a program to calculate the sum of following series where n is input by user.
# 1/1! + 2/2! + 3/3! + ..... N/N!
n=int(input("Enter value for n : "))
sum_series = 0
for i in range (1,n+1):
    fact = 1
    for j in range (1,i+1):
        fact *= j
    sum_series += i/fact
print("Sum of the series is : ",sum_series)         
