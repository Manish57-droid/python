# Python program to
# print given pattern

# Function to print
# pattern for
# given value of n
def pattern(n):
	
	# Outer "for" loop
	# for number of rows
	i = 1
	while i <= n:
	
		k = 65;
		m = 1;

		# Inner "for" loop for
		# number of columns
		j = 1
		while j <= (2 * n):

			# Logical execution
			# i.e, condition
			if (j >= n + 1 - i) and (j <= n + i):
				if (j <= n):

					# Print the alphabets
					print(chr(k)),
					k += 1
				else:

					# Print the numbers
					print(m),
					m += 1
			
			else:
				print(" "),
			j += 1
		i += 1

		# Print the next
		# line
		print("\n")
	

# Driver Code
def main():
	n = 7
	
	# Function calling
	pattern(n)

if __name__=="__main__":
	main()
	

