import java.util.Scanner;

public class ArrayReverse {
    public static void main(String[] args) {
        Scanner scn=new Scanner(System.in);
        int n=scn.nextInt();
        int[] array=new int[n];
        for (int i = 0; i < array.length; i++) {
            array[i]=scn.nextInt();
        }
        System.out.println("printing in reverse");
        for (int i = array.length-1; i >= 0; i--) {
            System.out.println(array[i]);
        }
        scn.close();
    }
}
