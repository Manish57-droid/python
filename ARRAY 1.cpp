
#include<iostream>
using namespace std;
int main ()
{
    int arr[10], n, i, sum = 0 ;
    cout << "Enter the size of the array : ";
    cin >> n;
for (i = 0; i < n; i++)
   { cout << "Enter the value of " << i << " th element : ";
      cin >> arr[i];}
    for (i = 0; i < n; i++)
    {
        sum += arr[i];
       
    }
    cout << "\nSum of all elements : " << sum;
   
    return 0;
}
