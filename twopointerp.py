def reverseArray(array):
    start, end = 0, len(array)-1
    while start< end:
        array[start], array[end] = array[end] , array[start]
        start += 1
        end -= 1
  
array = [10, 20, 30, 40, 50]      
reverseArray(array)
print(array)