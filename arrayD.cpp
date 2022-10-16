#include <iostream>
using namespace std;
int main()
{
    int A[]= {2,4,3,5,6,8} ;
    for(int &x: A)
      cout<<++x<<endl;
      
      return 0;
}