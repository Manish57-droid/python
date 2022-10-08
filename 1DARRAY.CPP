#include<iostream.h>
#include<conio.h>
main()
{
int a[10],n,i;
clrscr();
cout<<"how many number you want to enter";
cin>>n;
cout<<"Ok enter the number one by one \n";
for(i=1;i<=n;i++)
cin>>a[i];
cout<<"array entered by u is \n";
for(i=1;i<=n;i++)
cout<<a[i]<<endl;
getch();
}