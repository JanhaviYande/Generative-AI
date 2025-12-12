# WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.
def check_armstrong(n):
    count = 0
    temp = n
    while temp > 0:
       d = temp%10
       temp //= 10
       count += 1

    temp = n   
    sum_pow = 0
    while temp > 0:
        d = temp%10
        temp //= 10
        sum_pow += (d**count)
    if sum_pow == n:
        return True
    else:
        return False
    
num = int(input("Enter a number : "))
if check_armstrong(num):
    print(num, "is armstrong number")  
else:
    print(num, "is not armstrong number")   
    