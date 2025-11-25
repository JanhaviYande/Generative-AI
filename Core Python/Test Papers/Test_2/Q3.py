# Write a program to accept basic salary of n employee.(n should be accepted from user)
# if basic salary is below 20000 then da-10%,ta-12% and hra-15%. otherwise da-15%,ta-18% and hra-20%.
# Based on this ,calculate the total salary of all employee

n = int(input("Enter number of employees : "))
total_salary = 0
for i in range(1,n+1):
    salary=float(input(f"Enter basic salary of employee {i} : "))
    if salary < 20000:
            da = 0.10 * salary
            ta = 0.12 * salary
            hra = 0.15 * salary
    else:
            da = 0.15 * salary
            ta = 0.18 * salary
            hra = 0.20 * salary
    total = salary + da +ta + hra
    total_salary += total
    print(f"Total salary for employee{i} : {total}")
print("Total salary of all employees : ",total_salary)


        

