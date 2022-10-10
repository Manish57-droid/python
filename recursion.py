# Program to calculate factorial of a number
# using a Non-Tail-Recursive function.
 
# non-tail recursive function
def Recur_facto(n):
   
    if (n == 0):
        return 1
   
    return n * Recur_facto(n-1)
   
# print the result
print(Recur_facto(6))
