r = 6
i = 0
while(i <= r - 1):
    j = 0
    while(j < i):
        print('', end=' ')
        j += 1
    k = i
    while(k <= r - 1):
        print('*', end=' ')
        k += 1
    print()
    i += 1
i = r - 1
while(i >= 0):
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while(k <= r - 1):
        print('*', end=' ')
        k += 1
    print('')
    i -= 1
