rows = 5
#for i in range(1, rows + 1):
#    print("*" * i)

#i = 0
#while i <= rows:
#    print("*" * i)
#    i += 1

for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

#(rows - i - 1) 5-0-1=4 (2*i+1) 2*0+1 = 1star
#(rows - i - 1) 5-1-1=3 (2*i+1) 2*1+1 = 3star
#(rows - i - 1) 5-2-1=2 (2*i+1) 2*2+1 = 5star
#............................................
