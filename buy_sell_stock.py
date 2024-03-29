'''
Problem - 
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a 
    different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example -
    Input: 
        prices = [7,1,5,3,6,4]
    Output: 
        5
'''


# Function to find profit

def max_profit(arr, n):
    max_ele = arr[-1]
    max_diff = 0

    for i in range(n - 1, -1, -1):
        ele = arr[i]
        if (max_ele - ele) < 0:
            max_ele = ele
        max_diff = max(max_ele - ele, max_diff)
    return max_diff


# Main Code
n = int(input("Enter Size of Array : "))
arr = list(map(int, input("Enter Elements : ").split()))

res = max_profit(arr, n)

print("Max Profit is : " + str(res))
