'''
Problem - 
    Given an array of integers. Find the Inversion Count in the array.
    Note : Inversion Count: For an array, inversion count indicates how far (or close) the
    array is from being sorted. If array is already sorted then the inversion count is 0. 
    If an array is sorted in the reverse order then the inversion count is the maximum. 
    Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
    Expected Time Complexity: O(N(logN))
    Expected Auxiliary Space: O(N)

Example -
    Input: 
        N = 5, arr[] = {2, 4, 1, 3, 5}
    Output: 
        3
'''


#Function to do merge sort
def _mergeSort(arr, temp_arr, left, right):
 
    # A variable inv_count is used to store
    # inversion counts in each recursive call
 
    inv_count = 0
 
    # We will make a recursive call if and only if
    # we have more than one elements
 
    if left < right:
 
        # mid is calculated to divide the array into two subarrays
        # Floor division is must in case of python
 
        mid = (left + right)//2
 
        # It will calculate inversion
        # counts in the left subarray
 
        inv_count += _mergeSort(arr, temp_arr,
                                    left, mid)
 
        # It will calculate inversion
        # counts in right subarray
 
        inv_count += _mergeSort(arr, temp_arr,
                                  mid + 1, right)
 
        # It will merge two subarrays in
        # a sorted subarray
 
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count
 
# This function will merge two subarrays
# in a single sorted subarray
def merge(arr, temp_arr, left, mid, right):
    i = left     # Starting index of left subarray
    j = mid + 1 # Starting index of right subarray
    k = left     # Starting index of to be sorted subarray
    inv_count = 0
 
    # Conditions are checked to make sure that
    # i and j don't exceed their
    # subarray limits.
 
    while i <= mid and j <= right:
 
        # There will be no inversion if arr[i] <= arr[j]
 
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1
 
    # Copy the remaining elements of left
    # subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
 
    # Copy the remaining elements of right
    # subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
 
    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
         
    return inv_count

# Function to find inversions
def inv(arr, n):
    temp_arr = [0]*n
    return(_mergeSort(arr,temp_arr,0,n-1))
    

# Main Code
n = int(input("Enter Size of Array : "))
arr = []*n
arr = list(map(int, input("Enter Array Elements : ").split()))

count = inv(arr, n)

print("Inversion Count is : " + str(count))
