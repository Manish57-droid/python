class Operation2{  
 int data=50;  
  
 void change(Operation2 op){  
 op.data=op.data+100;//changes will be in the instance variable  
 }  
     
    
 public static void main(String args[]){  
   Operation2 op=new Operation2();  
  
   System.out.println("before change "+op.data);  
   op.change(op);//passing object  
   System.out.println("after change "+op.data);  
  
 }  
}  
