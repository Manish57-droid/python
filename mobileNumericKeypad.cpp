// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
    

	public:
// 	int dp[10][26];
	
// // 	bool possible(int keypad[4][3],int i , int j)
// // 	{
// // 	    if((i>=0 && j>=0) &&  (i<4 && j < 3)  ){
// // 	        if(keypad[i][j] == -1) return false;
// // 	        else return true;
// // 	    }
// // 	}
	
	
// 	long long fun(int N,int i , int j,int keypad[4][3]){
// 	    if(N==1)    return 1;
// 	    if(dp[ keypad[i][j] ][N] != -1) return dp[ keypad[i][j] ][N];
// 	    long long a=fun(N-1,i,j,keypad);
// 	    long long b=0;
// 	    long long c=0;
// 	    long long d=0;
// 	    long long e=0;
// 	    //same button
	    
	    
// 	   // //up
// 	   // int newi=i-1;
// 	   // int newj=j;
// 	   // if(possible(keypad,newi,newj)){
// 	   //     ans+=fun(N-1,newi,newj,keypad);
// 	   // }
	    
// 	   // //down
// 	   // newi=i+1;
// 	   // newj=j;
// 	   // if(possible(keypad,newi,newj)){
// 	   //     ans+=fun(N-1,newi,newj,keypad);
// 	   // }
	    
// 	   // //left
// 	   // newi=i;
// 	   // newj=j-1;
// 	   // if(possible(keypad,newi,newj)){
// 	   //     ans+=fun(N-1,newi,newj,keypad);
// 	   // }
	    
// 	   // //right
// 	   // newi=i;
// 	   // newj=j+1;
// 	   // if(possible(keypad,newi,newj)){
// 	   //     ans+=fun(N-1,newi,newj,keypad);
// 	   // }
	   
// 	if(i-1>=0 && keypad[i-1][j] != -1)  b=fun(N-1,i-1,j,keypad);
//     if(j-1>=0 && keypad[i][j-1] != -1)  c=fun(N-1,i,j-1,keypad);
//     if(i+1<4 && keypad[i+1][j] != -1)  d=fun(N-1,i+1,j,keypad);
//     if(j+1<3 && keypad[i][j+1] != -1)  e=fun(N-1,i,j+1,keypad);
// 	    return dp[ keypad[i][j] ][N] = a+b+c+d+e;
// 	}
	
	
	
// 	long long getCount(int N)
// 	{
// 		dp[10][N+1];
//       memset(dp,-1,sizeof(dp));
// 		int keypad[4][3] ={(1,2,3),
// 	                       (4,5,6),
// 	                       (7,8,9),
// 	                       (-1,0,-1)};
//       long long ans=0;
       
//       for(int i=0;i<4;i++)
//       {
//           for(int j=0;j<3;j++)
//           {
//               if(keypad[i][j] != -1){
//                     ans+=fun(N,i,j,keypad);
//               }
//           }
//       }
//       return ans;
// 	}

long long dp[26][10];
	long long fun(int n,int i){
	    if(n==0) return 1;
	    if(dp[n][i]!=-1) return dp[n][i];
	    if(i==0) return dp[n][i] = fun(n-1,0)+fun(n-1,8);
	    if(i==1) return dp[n][i] = fun(n-1,1)+fun(n-1,2)+fun(n-1,4);
	    if(i==2) return dp[n][i] = fun(n-1,2)+fun(n-1,1)+fun(n-1,3)+fun(n-1,5);
	    if(i==3) return dp[n][i] = fun(n-1,3)+fun(n-1,2)+fun(n-1,6);
	    if(i==4) return dp[n][i] = fun(n-1,4)+fun(n-1,1)+fun(n-1,5)+fun(n-1,7);
	    if(i==5) return dp[n][i] = fun(n-1,5)+fun(n-1,2)+fun(n-1,4)+fun(n-1,6)+fun(n-1,8);
	    if(i==6) return dp[n][i] = fun(n-1,6)+fun(n-1,3)+fun(n-1,5)+fun(n-1,9);
	    if(i==7) return dp[n][i] = fun(n-1,7)+fun(n-1,4)+fun(n-1,8);
	    if(i==8) return dp[n][i] = fun(n-1,8)+fun(n-1,5)+fun(n-1,7)+fun(n-1,9)+fun(n-1,0);
	    if(i==9) return dp[n][i] = fun(n-1,9)+fun(n-1,6)+fun(n-1,8);
	    
	}
	
	long long getCount(int n)
	{
		// Your code goes here
		memset(dp,-1,sizeof(dp));
	    long long ans = 0;
		for(int i = 0;i<=9;i++) ans+=fun(n-1,i);
	
	    return ans;
	}

};

// { Driver Code Starts.
int main() 
{
   	
   
   	int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;

       

	    Solution ob;
	    cout << ob.getCount(n) << "\n";
	     
    }
    return 0;
}
  // } Driver Code Ends