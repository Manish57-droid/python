"""
Expected O/P: 

   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * *

"""


s = int(input("Please enter the number of rows : "))
  # input here is 5 
  
t = s - 2  

for i in range(s, -1 , -1):  
    for j in range(t, 0 , -1):  
        print(end=" ")  
    t = t + 1  
    for j in range(0, i+1):  
        print("* " , end="")  
    print()  
  
t = 2 * s - 2   
for i in range(0, s):  
    for j in range(0, t):  
        print(end=" ")  
    
    t = t - 1  
    for j in range(0, i + 1):  
        print("* ", end="")  
    print("")   
