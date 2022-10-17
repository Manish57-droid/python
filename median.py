n = int(input("Enter the no. of n : "))
a=[]
print("Enter the elements : ")
for i in range(n):
    x = int(input())
    a.append(x)
for i in range (n):
    for j in range(i + 1, n):
        if(a[i] > a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
if (n%2!=0):
    median=a[n//2]
    print(median)
else:
    m=a[(n-1)//2] + a[n//2]
    median = m/2
    print(median)
