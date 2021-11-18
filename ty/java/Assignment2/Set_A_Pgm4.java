import java.util.Scanner;

public class Set_A_Pgm4 {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.print("\nEnter first name :");
        String firstName = scn.nextLine();

        System.out.print("\nEnter middle name :");
        String name = scn.nextLine();

        System.out.print("\nEnter last name :");
        String lastName = scn.nextLine();

        String firstLetter = name.substring(0, 1);
        firstLetter = firstLetter.toUpperCase();
        String remainingLetter = name.substring(1);
        remainingLetter = remainingLetter.toLowerCase();

        String middleName = firstLetter + remainingLetter;

        System.out.println(lastName + " " + firstName + " " + middleName);
        scn.close();
    }
}
