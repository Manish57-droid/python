#include<stdio.h>
void main()
{float p, r, t, x;
printf("enter principle:");
scanf("%f",&p);
printf("enter rate:");
scanf("%f",&r);
printf("enter time:");
scanf("%f",&t);
x=p*r*t/100;
printf("simple interest:%2f",x);
}