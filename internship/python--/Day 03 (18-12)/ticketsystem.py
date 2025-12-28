#assigning the values to variables
adults_price = 100  
kids_price = 50

print("Welcome! How many ticket you want")
tickets = int(input("Enter your tickets:")) #ask the number of tickets

adults = int(input("Enter number of adults: "))  #ask how many adults and children
kids = int(input("Enter number of kids: "))


if tickets != adults + kids: #if tickets doesn't match number of adults and children
    print("number of ticket does not matching")
else:
    total_amount = (adults * adults_price) + (kids * kids_price)  #calculating total amount of tickets

print("\nticket details")
print("Adults", adults, "x", adults_price, "=", adults * adults_price) #printing statement in neat format
print("kids", kids, "x", kids_price, "=", kids * kids_price)
print("Total tickets:", tickets)
print("Total amount:", total_amount)

  
