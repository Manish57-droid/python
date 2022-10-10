# Python Program to Print Half Diamond Star Pattern
 
rows = int(input("Enter Hollow Half Diamond Pattern Rows = "))

print("Hollow Half Diamond Star Pattern") 
i = 0
while(i < rows):
    j = 0
    while(j <= i):
        if i == j or j == 0:
            print('*', end = '')
        else:
            print(' ', end = '')
        j = j + 1
    i = i + 1
    print()

i = 1
while(i < rows):
    j = i
    while(j < rows):
        if i == j or j == rows - 1:
            print('*', end = '')
        else:
            print(' ', end = '') 
        j = j + 1
    i = i + 1
    print()
