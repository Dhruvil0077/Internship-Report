fruits = ["Apple", "Banana", "cherry", "mango"]
print("orignal list:", fruits)

#accessing the element through the indexing
print("Accessing list:",fruits[1])

#slicing the list from indexing 
print("Slicing:", fruits[0:2])

#adding the element to the list
fruits.append("orange")
print("Ading new element:",fruits)

New_list = fruits.remove("Apple")
print("Removing element:",fruits)

fruits.pop()
print(fruits)

number = [9, 8, 7, 5, 2, 3, 1, 6, 4]
number.sort()
print("Sorting list:",number)

word = "Mango"
if word in fruits:
    print(f"{word} is present in list")
else:
    print(f"{word} is not present in list")
