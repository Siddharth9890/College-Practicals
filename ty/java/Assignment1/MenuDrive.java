import java.util.Scanner;
import java.lang.Math;

public class MenuDrive {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int choice;
        do {
            System.out.println("Enter 1 for volume of cylinder");
            System.out.println("Enter 2 for factorial");
            System.out.println("Enter 3 for armstrong");
            System.out.println("Enter 4 for exit");
            choice = scn.nextInt();

            switch (choice) {
            case 1:
                System.out.println("Enter radius");
                int radius = scn.nextInt();
                System.out.println("Enter height");
                int height = scn.nextInt();
                volume(radius, height);
                break;
            case 2:
                System.out.println("Enter number for finding the factorial");
                int number = scn.nextInt();
                System.out.println(factorial(number));
                break;
            case 3:
                System.out.println("Enter number for finding the armstrong");
                int num = scn.nextInt();
                armstrong(num);
                break;
            }
        } while (choice != 4);
        scn.close();
    }

    public static void volume(int radius, int height) {
        final double pi = Math.PI;
        double volume = pi * radius * radius * height;
        System.out.println(volume);
    }

    public static int factorial(int number) {
        if (number == 0)
            return 1;

        return factorial(number - 1) * number;

    }

    public static void armstrong(int number) {
        int check, rem, sum = 0;

        check = number;

        while (check != 0) {
            rem = check % 10;
            sum = sum + (rem * rem * rem);
            check = check / 10;
        }

        if (sum == number)
            System.out.println(number+"is an armstrong number.");
        else
            System.out.println(number+"is not an armstrong number.");
    }
}
