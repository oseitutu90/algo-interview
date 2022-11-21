public class ReapeatedString {
    public static void main(String[] args) {
       
        System.out.println(repeatedString("aba",10));
    }
    
 public static int repeatedString(String s, Integer n){
        if((s.length() == 1) && ("a".equals(s))){
            return n;
        } else{
            int count = 0;
            for(int i = 0; i < s.length(); i++){
                if(s.charAt(i) == 'a'){
                    count++;
                }
            }
            int total = count * (n / s.length());
            int remainder = n % s.length();
            for(int i = 0; i < remainder; i++){
                if(s.charAt(i) == 'a'){
                    total++;
                }
            }
            return total;
        }
 }
}
