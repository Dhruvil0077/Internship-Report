print("Welcome to Banking system")
salary = int(input("Enter your salary:")) #take the salary from the person
credit = int(input("Enter your credit score(300-700):")) 

#check if person has requirement salary needed for loan.if not it not approved the loan
if salary >= 30000:
    print("you are allow for loan")

    #if salary requirement approved we check for credit score higher the score lesser the interest
    if credit >= 700:
        print("your loan amount are approved")
    elif credit >= 600:
        print("your loan are approved but with interest 5%")
    elif credit >= 500:
        print("you have to give interest of 10%")
    else:
        print("you don't have enough credit")
else:
    print("You don't enough salary")