#include<stdio.h>
#include<conio.h>
#include<malloc.h>
struct node
{
	int info;
	struct node *next;
}*rear=NULL,*front=NULL;
void main()
{
	int ch;
	clrscr();
	while(1)
	{
		printf("\n1.Insert item");
		printf("\n2.Delete item");
		printf("\n3.Display");
		printf("\n4.Quit");
		printf("\nEnter your choice=");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1:
				insert_item();
				break;
			case 2:
				del_item();
				break;
			case 3:
				display();
				break;
			case 4:
				exit(1);
			default:
				printf("\n Wrong choice Try again!!!!");
		}
	}
}
insert_item()
{
	struct node *temp;
	int item;
	temp=(struct node *)malloc(sizeof(struct node));
	printf("\n Enter item to be inserted= ");
	scanf("%d",&item);
	temp->info=item;
	temp->next=NULL;
	if(front==NULL)
		front=temp;
	else
		rear->next=temp;
	rear=temp;
}
del_item()
{
	struct node *temp;
	if(front==NULL)
		printf("\n Queue underflow");
	else
	{
		temp=front;
		printf("\n Element after deletion is=%d",temp->info);
		front=front->next;
		free(temp);
	}
}
display()
{
	struct node *trav;
	if(front==NULL)
		printf("\n Queue is empty");
	else
	{
		printf("\ncontents of queue are=\n");
		for(trav=front;trav!=NULL;trav=trav->next)
		{
			printf("%d",trav->info);
		}
	}
}