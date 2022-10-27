def count_occurence(l):
    occur={}
    for i in l:
        occur[i]=occur.get(i,0)+1
    for key,value in occur.items():
        print(key," occurs ",value," times")
size=int(input("Enter the number of elements you want to add in list :: "))
l=[]
for i in range(size):
    ele=int(input("Enter the element :"))
    if(ele>=1 and ele<=20):
        l.append(ele)
count_occurence(l)
