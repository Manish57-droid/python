d = 256
def search(pat, txt, q):
	M = len(pat)
	N = len(txt)
	i = 0
	j = 0
	p = 0 
	t = 0 
	h = 1
	for i in range(M-1):
		h = (h*d) % q
	for i in range(M):
		p = (d*p + ord(pat[i])) % q
		t = (d*t + ord(txt[i])) % q

	# Slide the pattern over text one by one
	for i in range(N-M+1):
		if p == t:
			# Check for characters one by one
			for j in range(M):
				if txt[i+j] != pat[j]:
					break
				else:
					j += 1

			# if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
			if j == M:
				print("Pattern found at index " + str(i))

		# Calculate hash value for next window of text: Remove
		# leading digit, add trailing digit
		if i < N-M:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q

			# We might get negative values of t, converting it to
			# positive
			if t < 0:
				t = t+q

if __name__ == '__main__':
	txt = "GEEKS FOR GEEKS"
	pat = "GEEK"

	# A prime number
	q = 101

	# Function Call
	search(pat, txt, q)
