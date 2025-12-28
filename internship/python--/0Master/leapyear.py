year = int(input("Enter the year:"))

if (year % 400 == 0 and year % 100 == 0):
    print("it is a leap year")
elif (year % 100 != 0 and year % 4 == 0):
    print("it is a leap year")
else:
    print("it is not leap year")

#import datetime   #using datetime module to run the preogram
#year = int(input("Enter the year:"))

#try:
#    datetime.date(year, 2, 29) #check the
#    print(f"Enter year {year} is a leap year :")
#except:
#   print("It is not a leap year:")