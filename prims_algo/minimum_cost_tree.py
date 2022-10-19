#Finding Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

##LOGIC:
# 1) Create a set Sthat keeps track of vertices already included in MST.
# 2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE. 
#    Assign key value as 0 for the first vertex so that it is picked first.
# 3) While S doesn’t include all vertices.

###program:
  
maxi=9999999        #maximum value which we can take=9999999.

n=int(input("Enter the number of nodes:"))

#It then creates an array with all possible paths to each node, which is stored in the variable "selected".
selected=[False for i in range(n)]        
def main(n,cost):
 n_edge=0
 selected[0]=True
 while n_edge<n-1:
 minimum=maxi
 x=y=0
  
  #Then it declares two boolean variables: one for whether or not x is selected, and another for y being selected.
 for i in range(n):
 if selected[i]:
 for j in range(n):
 if not selected[j] and cost[i][j]:
 if minimum>cost[i][j]:
 minimum=cost[i][j]
 x=i
 y=j
 print(x,'-->',y,':',cost[x][y])
 selected[y]=True
 n_edge+=1
cost=[[int(x) for x in input().split()]
      
#For each iteration of the for loop, if selected[i] is true then a for loop iterate through all nodes in a range of n
 for j in range(n)]
for i in range(n):
 for j in range(n):
 if cost[i][j]==0:
 cost[i][j]=maxi
print("The shortest path using Prim's Algorithm is :\n")
main(n,cost)



OUTPUT:
  Enter the number of nodes:
    99  3  2
    3  99  4
    2  4  99
  The shortest path using Prim's Algorithm is :
  0 --> 2 : 2
  0 --> 1 : 3
    
    
    
    
    
    
    
