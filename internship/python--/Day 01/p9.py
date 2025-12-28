num = int(input("Enter number: "))

if num <= 1:
    print("Not prime")

elif num == 2 or num == 3:
    print("Prime")

elif num % 2 == 0 or num % 3 == 0:
    print("Not prime")

else:
    print("Prime")
