#Program to print subsets of an array using bit-manipulation

ar = [1,2,3]
length = (1<<len(ar))

for i in range(0,length):
    num = i
    position = 0
    t_arr = []
    while num!= 0:
        if num & 1<<0 :t_arr.append(ar[position])
        num = num>>1
        position+=1
    print(t_arr)    