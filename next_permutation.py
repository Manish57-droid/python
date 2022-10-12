'''
Problem - 
    Implement next permutation, which rearranges numbers into the lexicographically next greater 
    permutation of numbers. If such an arrangement is not possible, it must rearrange it as the 
    lowest possible order (i.e., sorted in ascending order). 
    The replacement must be in place and use only constant extra memory.

Example -
    Input: 
        nums = [1,2,3]
    Output: 
        [1,3,2]
'''


# Function to merge intervals

def next_permutation(arr, n):
    for i in range(n-2, 0, -1):
        if arr[i] < arr[i + 1]:
             break
    if i < 0:
        arr.reverse()
    else:
        for j in range(n-1,i,-1):
            if arr[j] > arr[i]:
                break
        arr[j], arr[i] = arr[i], arr[j]
        arr[i+1:n-1].reverse()


# Main Code
n = int(input("Enter Size of Array : "))
arr = list(map(int, input("Enter Array Elements : ").split()))

next_permutation(arr, n)

print("Next Purmuation of Array is : ")
for i in arr:
    print(i, end = " ")
