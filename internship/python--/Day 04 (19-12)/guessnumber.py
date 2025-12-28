secret_number = 7

for i in range(5):
    ask = int(input("Enter the number:"))

    if ask == secret_number:
       print("You got it right")
       break
    else:
        print("Try again!")
print("game over")

attempt = 1
while attempt <= 5:
    ask = int(input("Enter the number:"))
    if ask == secret_number:
        print("You got it right")
        break
    else:
        print("Try again!")
    attempt += 1
