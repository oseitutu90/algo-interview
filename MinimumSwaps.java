public class MinimumSwaps {
 public static void main(String[] args) {
    int[] arr = {7, 1, 3, 2, 4, 5, 6};
    System.out.println(minimumSwaps(arr));
 }   

    public static int minimumSwaps(int[] arr) {
        int count = 0;
        for(int i = 0; i < arr.length; i++){
            if(arr[i] != i + 1){
                int temp = arr[i];
                arr[i] = arr[temp - 1];
                arr[temp - 1] = temp;
                count++;
            }
        }
        return count;
    }
}
