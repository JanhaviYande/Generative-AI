# Sum of all prime numbers between 1 to n

def sum_of_prime(n):
    sum = 0
    for num in range(2,n+1):
        isprime = True
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                isprime = False
                break
        if isprime:
            sum += num    
    return sum

num = int(input("Enter a number : "))
print("sum of prime numbers between 1 to", num, ":",sum_of_prime(num))