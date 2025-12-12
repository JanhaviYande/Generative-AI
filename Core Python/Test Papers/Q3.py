num = 22
for i in range(1,num+1):   
    for j in range(1,num+1):
        if i == 1:
            print("*",end=" ")
        elif i ==num:
            print("*",end=" ")
        else:
            if j == num-i+1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()    
