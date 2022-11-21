public class interviewTwoStrings {
    public static void main(String[] args) {
        String str2 = "Hello the world is not as blue as you think";
        String str1 = "world";

        // System.out.println(twoStrings(str1, str2));
        System.out.println(str1.substring(0, str1.length()));

        
    }
    /*
     * takes in two strings and returns the index of the first 
     * occurence of the first string in the second string
     */

     public static int twoStrings(String str1, String str2) {
            if (str1.length() > str2.length()) {
                return -1;
            }
            for (int i = 0; i < str2.length(); i++) {  // O(n)
                if (str2.charAt(i) == str1.charAt(0)) { // O(1)
                    if (str2.substring(i, i + str1.length()).equals(str1)) {
                        return i;
                    }
                }
            }
            return -1;
     }
}
