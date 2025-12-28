marks = int(input("Enter marks of students:"))

if marks >= 80:
    print("You score distinction:")
elif marks >= 60:
    print("You score first class:")
elif marks >= 35:
    print("You score second class:")
else:
    print("You fail")