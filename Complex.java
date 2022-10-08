
import java.util.*;

public class Complex {
	float real;
	float imag;
	Scanner scn = new Scanner(System.in);
	void setdata() {
		
		System.out.println("enter the real value of complex number ");
		real= scn.nextFloat();
		System.out.println("enter the imaginary value of complex number ");
		imag= scn.nextFloat();
		
	}
	
	void add(float a,float b,float c,float d) {
		real= a+c;
		imag= b+d;
	}
	
	void substract(float a,float b,float c,float d) {
		real= a-c;
		imag= b-d;
	}
	
	void multiply(float a,float b,float c,float d) {
		real = (a*c)-(b*d);
		imag = (a*d)+(b*c);
	}
	
	void divide(float a,float b,float c,float d) {
		real = ((a*c)+(b*d))/((c*c)+(d*d));
		imag = ((b*c)-(a*d))/((c*c)+(d*d));
	}
	
	void getdata() {
		if(imag>=0) {
			System.out.println(real+"+"+imag+"i");
		}
		else {
			System.out.println(real+""+imag+"i");
		}
	}

	public static void main(String[] args) {
		try (Scanner scn1 = new Scanner(System.in)) {
			Complex x2 = new Complex();
			Complex x1= new Complex();
			Complex addition= new Complex();
			Complex substraction = new Complex();
			Complex division = new Complex();
			Complex multiplication = new Complex();
			
			
			x1.setdata();
			x2.setdata();
			
			System.out.println("complex number1 is ");
			x1.getdata();
			System.out.println("complex number 2 is ");
			x2.getdata();
			
			
			int ans=1;
			while(ans==1) {
				System.out.println("choose the operation to perform \n1.addtion\n2.substraction\n3.multiplication\n4.division");
				int a= scn1.nextInt();
				switch (a){
				case 1:
					addition.add(x1.real,x1.imag,x2.real,x2.imag);
					System.out.println("addition of complex1 and complex2 is ");
					addition.getdata();
					break;
					
				case(2):
					substraction.substract(x1.real,x1.imag,x2.real,x2.imag);
					System.out.println("substraction of complex2 from complex1 is ");
					substraction.getdata();
					break;
				
				case(3):
					multiplication.multiply(x1.real,x1.imag,x2.real,x2.imag);
					System.out.println("multiplication of comlex1 and complex2 is ");
					multiplication.getdata();
					break;
					
				case(4):
					division.divide(x1.real,x1.imag,x2.real,x2.imag);
					if((x2.real==0)&&(x2.imag==0)) {
						System.out.println("can't divide by zero");
					}
					else {
						System.out.println("on division of complex1 by complex2, we get ");
						division.getdata();
					}
					
				default:
					System.out.println("Invalid option choosen!!!!");
					
				}
				
				
				
				System.out.println("do you want to check more?\n(press 1 for yes/2 for no)");
				ans= scn1.nextInt();
				if(ans==2) {
					break;
				}
			
}
		}
		//System.out.println("data type if marks is");
		System.out.println("\nThank you");
	
}
}