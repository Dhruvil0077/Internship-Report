number = [1, 2, 2, 3, 3, 4, 5, 6, 6]
new_list = []

for i in number:
    if i not in new_list:
        new_list.append(i)
        
print(new_list)
