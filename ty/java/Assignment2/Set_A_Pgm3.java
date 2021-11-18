import java.util.Arrays;

public class Set_A_Pgm3 {
    public static void main(String args[]) {

        int array[] = new int[5];

        for (int i = 0; i < 5; i++) {
            array[i] = Integer.parseInt(args[i]);
        }

        Arrays.sort(array);

        System.out.println("Sorted Array :");

        for (int i = 0; i < 5; i++) {
            System.out.println(array[i]);
        }

    }
}