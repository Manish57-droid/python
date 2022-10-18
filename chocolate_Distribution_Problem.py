def findMinDiff(arr, n, m):
	if (m == 0 or n == 0):
		return 0
	arr.sort()
	if (n < m):
		return -1
	min_diff = arr[n-1] - arr[0]
	for i in range(len(arr) - m + 1):
		min_diff = min(min_diff, arr[i + m - 1] - arr[i])
	return min_diff

if __name__ == "__main__":
	arr = [12, 4, 7, 9, 2, 23, 25, 41,
		30, 40, 28, 42, 30, 44, 48,
		43, 50]
	m = 7 # Number of students
	n = len(arr)
	print("Minimum difference is", findMinDiff(arr, n, m))
