package MergeSort;

public class MergeSort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] array= {10,56,33,566,14,12}; 
 int[] ans= mergeSort(array,0,array.length-1);
   for(int x=0;x<ans.length;x++)
   {
	   System.out.print(ans[x]+" ");
   }
	}
	public static int[] mergeTwoSortedArrays(int[] arr1,int[] arr2) {
		int[] res=new int[arr1.length+arr2.length];
		int i=0;
		int j=0;
		int k=0;
		
		
		while(i<arr1.length && j<arr2.length) {
			if(arr1[i]<=arr2[j])
			{
				res[k]=arr1[i];
				i++;
				k++;
			}
			else
			{
				res[k]=arr2[j];
				j++;
				k++;
			}
		}
		if(i==arr1.length) {
			while(j<arr2.length) {
				res[k]=arr2[j];
				k++;
				j++;
			}
		}
		if(j==arr2.length) {
			while(i<arr1.length) {
				res[k]=arr1[i];
				k++;
				i++;
			}
		}
		return res;
	}
	
	public static int[] mergeSort(int[] arr,int lo,int hi) {
		if(lo==hi)
		{
			int[] baseResult=new int[1];
			baseResult[0]=arr[lo];
			return baseResult;
		}
		
		int mid=(lo+hi)/2;
		
		int[] fh=mergeSort(arr,lo,mid);
		int[] sh=mergeSort(arr,mid+1,hi);
		
		int[] merge=mergeTwoSortedArrays(fh,sh);
		return merge;
	}

}
