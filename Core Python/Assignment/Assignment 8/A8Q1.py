# Write a program to calculate area of rectangle

def area_of_rect(l,b):
    area = l * b
    return area

length = float(input("Enter length of rectangle : "))
breadth = float(input("Enter breadth of rectangle : "))
print("Area of rectangle : ",area_of_rect(length,breadth))