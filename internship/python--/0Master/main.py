program = {
    1:"ticketsystem",
    2:"vote",
    3:"week",
    4:"bank",
    5:"leapyear"
}
for key,value in program.items():
    print(f"{key}:{value}")
choice = int(input("Enter your choice:"))
if choice == 1:        #assigning the values to variables
    import ticketsystem
elif choice == 2:
    import vote
elif choice == 3:
    import week   
elif choice == 4:
    import bank
elif choice == 5:
    import leapyear
