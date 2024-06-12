//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
    public:
//my try
//     int dp[1000005][1000005];
//     int helper(int csum,int tsum,int arr[],int n,vector<vector<int>> dp){
//         //base condition
//         if(n<0){
//             return abs(tsum-csum-csum);
//         }
//         if(dp[n][csum]!= -1)    return dp[n][csum];
        
//         int val1 = helper(csum+arr[n],tsum,arr,n-1,dp);
//         int val2 = helper(csum,tsum,arr,n-1,dp);
        
//         return  dp[n][csum] = min(val1,val2);
        
//     }
    
    
  
// 	int minDifference(int arr[], int n)  { 
	    
// 	    int sum=0;
// 	    int tsum=0;
// 	    for(int i=0;i<n;i++)
// 	    {
// 	        tsum+=arr[i];
// 	    }
// 	    vector<vector<int>> dp(n+1, vector<int>(tsum+1, -1));
	    
// 	    return helper(sum,tsum,arr,n-1,dp);
// 	} 
//_______________________________________________________________________________________________________
	int knapsack(int arr[], int n, int currsum, int t, vector<vector<int>> & dp){
        if(n==0){
            return currsum;
        }
        
        if(dp[n][currsum] != -1) return dp[n][currsum];
        
        int a = knapsack(arr, n-1, currsum+arr[n-1], t, dp);
        int b = knapsack(arr, n-1, currsum, t, dp);
        
        if(n==1)
        return dp[n][currsum] = min(abs(t-2*a), abs(t-2*b));
        
        else return dp[n][currsum] = min(dp[n-1][currsum+arr[n-1]], dp[n-1][currsum]);
    }
    
	int minDifference(int arr[], int n)  { 
	    int t = 0;
	    for(int i=0; i<n; i++) t+=arr[i];
	    vector<vector<int>> dp(n+1, vector<int>(t+1, -1));
	    
	    return knapsack(arr, n, 0, t, dp);
	}
};




//{ Driver Code Starts.
int main() 
{
   
   
   	int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;

        int a[n];
        for(int i = 0; i < n; i++)
        	cin >> a[i];

       

	    Solution ob;
	    cout << ob.minDifference(a, n) << "\n";
	     
    }
    return 0;
}
// } Driver Code Ends