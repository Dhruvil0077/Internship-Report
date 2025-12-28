pin = 1234
balance = 20000
history = []

entered_pin = int(input("Enter your pin:"))
if entered_pin != pin:
    print("Invalid pin")
    exit()
else:
    print("Select your choice:")

    
    while True:
        print("1.Check Balance")
        print("2.Deposit Amount")
        print("3.Withdrawn money")
        print("4. Transaction history")
        print("5.change pin")

        choice = int(input("Enter the choice(1-5):"))
        if choice == 1:
            print(f"Your current Balance is:{balance}")
        elif choice == 2:
            amount = int(input("Enter the amount:"))
            balance += amount
            history.append(f"+{amount}")
            print(f"Your money is deposited")
        elif choice == 3:
            amount = int(input("Enter the amount:"))
            if amount > balance:
                print("Insufficient Balance")
            else: 
                balance -= amount
                history.append(f"-{amount}")
                print(f"money withdrawn successfully{amount}")
        elif choice == 4:
            print(f"Transaction history{history}")
            #for entry in history:
            #   print(entry)
        else:
            print("Invalid Choice")
            break