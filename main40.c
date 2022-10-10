#include<stdio.h>
void main()
{
	int a=2,b=6;
	label:
		printf("%d  ",a);
		a=a+b;
		b=b+4;
		if(a<=50)
		{
			goto label;
		}
}
