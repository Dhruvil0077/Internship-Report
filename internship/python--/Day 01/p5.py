print("Welcome to Calculator")

num1 = float(input("Enter your number1:"))
num2 = float(input("Enter your number2:"))

choice = input("What you like to do +, -, *, /, %: ")

if choice == "+":
    print("The sum of number is:", num1 + num2)
elif choice == "-":
    print("The subtraction of numbers is:", num1 - num2)
elif choice == "*":
    print("The multipy of numbers is:", num1 * num2)
elif choice == "/":
    print("The division of numbers is:", num1 / num2)
elif choice == "%":
    print("The module of numbers is:", num1 % num2)
else:
    print("your choice is not present")

print("Thank you")