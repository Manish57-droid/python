package Stacks;

public class StackUsingArrays {

private int[] data;
private int top;

public static  final int Default_Capacity=10;

public StackUsingArrays throws Exception ()
	{
		this.(Default_Capacity);
	}
public StackUsingArrays(int capacity) throws Exception()
	{ if(capacity<1)
		throw new Exception("Invalid Capacity");
	this.data=new int[capacity];
	top=-1;
	}
public int size()
{
	return this.top+1;
}

public boolean isEmpty() {
	return this.size()==0;
}

public void push(int value) {
	if(this.size()==data.length)
		throw new Exception("Stack is Full");
	this.top++;
	this.data[this.top]=value;
}

public int top() throws Exception{
	if(this.size()==0)
		throw new Exception("Stack is Empty");
	int rv=this.data[this.top];
	this.data[this.top]=0;
	this.top--;
	return rv;
}

}

