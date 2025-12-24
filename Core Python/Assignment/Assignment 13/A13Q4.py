# Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).
n = int(input("Enter a number : "))
result = {}
for i in range (1,n+1):
    result[i] = i*i
print(result)