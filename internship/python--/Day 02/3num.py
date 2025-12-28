#Finding the maximum number

num1 = int(input("Enter the number1:"))  # taking 3 numbers from the user 
num2 = int(input("Enter the number2:"))
num3 = int(input("Enter the number3:"))

if num1 > num2:  # using if inside other if statement for checking 3 numbers
    if num1 > num3:
        print("Number1 is maximum:") #if both if condition is true then number1 is maximum
elif num2 > num3:
    print("Number2 is maximum:")
else:
    print("Number3 is maximum:")