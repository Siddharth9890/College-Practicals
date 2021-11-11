
public class Set_A_Pgm3 {
    public static void sort(int[] array, int n) {

        int temp = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < (n - i); j++) {
                if (array[j - 1] > array[j]) {
                    {
                        temp = array[j - 1];
                        array[j - 1] = array[j];
                        array[j] = temp;
                    }
                }

            }
        }
    }

    public static void main(String[] args) {
        int n = 5;
        int[] array = new int[n];
        for (int i = 0; i < 5; i++) {
            array[i] = Integer.parseInt(args[i]);
        }
        for (int i = 0; i < n; i++) {
            System.out.println(array[i]);
        }
        sort(array, n);
        for (int i = 0; i < n; i++) {
            System.out.println(array[i]);
        }

    }
}
