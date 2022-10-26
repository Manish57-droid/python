#include<iostream>
using namespace std;
int main(){
    int n;                  // to print right triangle
    cin>>n;
    for(int i=1;i<=n;i++){
        for(int j=0;j<n-i;j++){
            cout<<" ";
        }
        for(int j=0;j<2*i-1;j++){
              cout<<"*";
        }
        cout<<endl;
    }
    // int n;                          //        *      to print right triangle
    // cin>>n;                         //       **
    // for(int i=1;i<=n;i++){          //      ***   
    //       for(int j=0;j<n-i;j++){   //     ****
    //         cout<<" ";
    //       }
    //       for(int j=0;j<i;j++){
    //         cout<<"*";
    //       }
    //       cout<<endl;
    // }

}