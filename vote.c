#include<stdio.h>
int main()
//program for voting
{
    int age;
    printf("enter your age:",age);
    scanf("%d",&age);
    if(age>=18)
    {
        printf("you are eligible to vote\n");

    }
    else if(age>=12)
    {
        printf("you are not even teenage");
    }
    else
    {


        printf("you cannot vote");
    }


    return 0;
}
