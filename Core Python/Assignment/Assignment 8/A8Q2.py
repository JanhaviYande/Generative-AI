# Write a program to calculate area of circle
import math
def area_of_circle(r):
    area = math.pi * r * r
    return area

radius = float(input("Enter radius of circle : "))
print("Radius of circle: ",area_of_circle(radius))