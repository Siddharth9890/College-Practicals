import java.lang.String;

public class StringMethods {
    public static void main(String[] args) {
        // LENGTH
        String s1 = "welcome";
        System.out.println(s1.length());
        String s2 = "welcome";
        // EQUALS USING HASHCODE
        if (s1 == s2) {
            System.out.println("same");
        } else {
            System.out.println("not same");
        }
        String s3 = new String("welcome");
        String s4 = new String("hello");
        // EQUALS USING EQUALS METHOD
        if (s3.equals(s4)) {
            System.out.println("same");
        } else {
            System.out.println("not same");
        }
        // CONCAT
        String result=s3.concat(s4);
        System.out.println(result);
        // CHAR AT
        char ch=result.charAt(1);
        System.out.println(ch);
    }
}
