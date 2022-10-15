"""

Pattern: 

*
**
* * 
*  *  
*   *
******


"""


#Code: 
n = 6
for i in range(1, n+1):
    for j in range(i):
        # print star only at start and end of the row
        if j == 0 or j == i-1:
            print('*', end='')
        # print only star if it's last row
        else:
            if i != n:
                print(' ', end='')
            else:
                print('*', end='')
    print()
    
