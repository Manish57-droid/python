N = int(input(“\nEnter the number of rows : “))
print()
print(“*”)
for i in range(1,N+1):
	for j in range(1, i+1):
		if(j == 1):
			print(“*”, end = “”)
	print(j,end = “”)

for j in range(i-1, 0, -1):
	print(j,end = “”)
	print(“*”)

for i in range(N-1, 0, -1):
	for j in range(1, i+1):
		if(j == 1):	
			print(“*”,end = “”)
		print(j,end = “”)

for j in range(i-1, 0, -1):
	print(j,end = “”)
		print(“*”)
print(“*\n”);
