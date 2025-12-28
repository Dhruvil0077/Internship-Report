age = int(input("Enter your age:"))
has_voter_id = (input("you have voter id (yes/no):"))

#check if person is 18+ and has a voter ID 
if age >= 18 and has_voter_id == "yes":  
    print("You are allow to vote")
else:
    print("you are not eligible to vote")

#
if not(age >= 18 and has_voter_id == "yes"):
    print("\n Reason")
    if age <= 18 and has_voter_id == "yes":
        print("you are underage (must be 18+)")
    elif age >= 18 and has_voter_id != "yes":
        print("you have no voter ID")
