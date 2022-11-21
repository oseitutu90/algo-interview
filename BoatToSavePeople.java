import java.util.Arrays;
import java.util.UUID;

public class BoatToSavePeople {
    public static void main(String[] args) {


        System.out.println(numRescueBoats(new int[]{3,2,1,3}, 4));
       
    }
 
    /**
     * 
     """Find the number of boats to save people."""
     */
    public static int numRescueBoats(int[] people, int limit) {
        int boats = 0;
        int lightestPersonIdx = 0;
        int heaviestPersonIdx = people.length - 1;
        Arrays.sort(people);
        while (heaviestPersonIdx >= lightestPersonIdx) {
            if (people[heaviestPersonIdx] + people[lightestPersonIdx] <= limit) {
                lightestPersonIdx++;
            }
            heaviestPersonIdx--;
            boats++;
        }
     
        return boats;
    }
}
