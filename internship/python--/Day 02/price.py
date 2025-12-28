#sperating the rupees and paise from the price
price = float(input("Enter the price:"))

rupees = int(price)  # convert the float number in integer by adding int.
paise =  (price - rupees) * 100   #subtracting the price from rupees , And multipying 100 to displace decimal point 

print("Rupees:", rupees)
print("paise:", paise)
