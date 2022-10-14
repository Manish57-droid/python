def maxCrossingSum(arr, l, m, h):
	sm = 0
	left_sum = -10000

	for i in range(m, l-1, -1):
		sm = sm + arr[i]

		if (sm > left_sum):
			left_sum = sm

	# Include elements on right of mid
	sm = 0
	right_sum = -1000
	for i in range(m, h + 1):
		sm = sm + arr[i]

		if (sm > right_sum):
			right_sum = sm
	return max(left_sum + right_sum - arr[m], left_sum, right_sum)


# Returns sum of maximum sum subarray in aa[l..h]
def maxSubArraySum(arr, l, h):
	#Invalid Range: low is greater than high
	if (l > h):
		return -10000
	# Base Case: Only one element
	if (l == h):
		return arr[l]

	# Find middle point
	m = (l + h) // 2
	return max(maxSubArraySum(arr, l, m-1),
			maxSubArraySum(arr, m+1, h),
			maxCrossingSum(arr, l, m, h))
arr = [2, 3, 4, 5, 7]
n = len(arr)

max_sum = maxSubArraySum(arr, 0, n-1)
print("Maximum contiguous sum is ", max_sum)
