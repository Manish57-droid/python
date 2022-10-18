# Print Pascal's Triangle in Python
 
# input n
n = 5
 
# iterarte upto n
for i in range(n):
    # adjust space
    print(' '*(n-i), end='')
 
    # compute power of 11
    print(' '.join(map(str, str(11**i))))
