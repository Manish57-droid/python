# hollow alphabet diamond pattern

size = 5
alpha = 65
num = 0

# upward hollow pyramid
for i in range(size):
    for j in range(size - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print(chr(alpha+num), end='')
            num += 1
        else:
            print(' ', end='')
    # set num to 0
    num = 0
    print()

# downward pyramid
for i in range(size - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(size - i - 1) - 1):
        if j == 0 or j == 2*(size - i - 1) - 2:
            print(chr(alpha+num), end='')
            num += 1
        else:
            print(' ', end='')
    # set num to 0
    num = 0
    print()
