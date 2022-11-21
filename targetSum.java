
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class targetSum {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int target = 10;
        int[] result = twoSum(arr, target);
        System.out.println(result[0] + " " + result[1]);

    }

    public static int[] twoSum(int[] arr, int target) {
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < arr.length; i++) {
            int complement = target - arr[i];
            if (set.contains(complement)) {
                return new int[]{ i, Arrays.binarySearch(arr, complement)};
            }
            set.add(arr[i]);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
