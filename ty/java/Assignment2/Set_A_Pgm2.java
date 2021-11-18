import java.util.*;

class Main {
    int rollNo;
    String name;
    float percentage;

    Main() {
        rollNo = 0;
        name = "";
        percentage = 0;
    }

    Main(int rollNo, String name, float percentage) {
        this.rollNo = rollNo;
        this.name = name;
        this.percentage = percentage;
    }

    void display() {
        System.out.println(rollNo + " " + name + " " + percentage);
    }

    float getPercentage() {
        return percentage;
    }

    public static void sort(Main s[], int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (s[j].getPercentage() > s[j + 1].getPercentage()) {
                    Main t = s[j];
                    s[j] = s[j + 1];
                    s[j + 1] = t;

                }
            }
        }
        for (int i = n - 1; i >= 0; i--)
            s[i].display();
    }

    public static void main(String args[]) {
        Scanner scn = new Scanner(System.in);

        System.out.println("Enter no.of students: ");
        int n = scn.nextInt();
        Main array[] = new Main[n];
        for (int i = 0; i < n; i++) {
            System.out.print("Enter rollNo.:");
            int rollNo = scn.nextInt();
            System.out.print("Enter name:");
            String name = scn.next();
            System.out.print("Enter percentage:");
            float per = scn.nextFloat();
            array[i] = new Main(rollNo, name, per);
        }
        Main.sort(array, n);
        scn.close();
    }
}