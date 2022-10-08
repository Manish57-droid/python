# right pascal triangle
n = 5

# upper triangle
for i in range(n):
    for j in range(i + 1):
        print('*', end="")
    print()
# lower triangle
for i in range(n):
    for j in range(n - i - 1):
        print('*', end="")
    print()
