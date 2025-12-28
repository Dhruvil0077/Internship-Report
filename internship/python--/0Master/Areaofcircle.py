import math   #import math for using the PI in program

choice = input("Enter the choice 1 for circle and 2 for trianlge") #user choose between 1 & 2 for specific task they want to do

# user choose 1 for area of circle 
if choice == "1":  
    radius = int(input("Enter the value of radius:"))
    Area_circle = math.pi * radius ** 2
    print(Area_circle)

#choose 2 for area of triangle
elif choice == "2":
     base = int(input("Enter the value of base:"))
     height = int(input("Enter the value of height:"))
     area_triangle = 0.5 * height * base
     print(area_triangle)