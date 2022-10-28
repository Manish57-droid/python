#include <bits/stdc++.h>
using namespace std;

int returnDuplicate(int arr[], int n)
{
    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        ans = ans ^ arr[i];
    }
    for (int i = 1; i < n; i++)
    {
        ans = ans ^ i;
    }
    return ans;
}
int main()
{
    int a[] = {1, 2, 3, 4, 4};
    cout << returnDuplicate(a, 5);
    return 0;
}
