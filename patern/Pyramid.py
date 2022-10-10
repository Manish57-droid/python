row = int(input('Enter number of rows required: '))

for i in range(row):
    for j in range(row-i):
        print(' ', end='') # printing space required and staying in same line
    
    for j in range(2*i+1):
        print('*',end='') # printing * and staying in same line
    print() # printing new line
