import java.util.Scanner;

class Student {
    static int cnt = 0;
    int rno;
    String name;
    double percentage;

    Student(int rno, String name, double percentage) {
        rno = this.rno;
        name = this.name;
        percentage = this.percentage;
    }

    Student() {
        rno = 0;
        name = null;
        percentage = 0.0;
    }

    static void sortStudent(Student s1[], int n, Student y) {
        int temp = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < (n - i); j++) {
                if (s1[j].percentage < s1[i].percentage) {
                    y = s1[i];
                    s1[i] = s1[j];
                    s1[j] = y;
                }

            }
        }
    }

    static void displayCount() {
        ++cnt;
        System.out.println("Object created :" + cnt);
    }

    void display() {
        System.out.println("Roll No: " + rno + "Name: " + name + "Percentage: " + percentage);
    }

}

public class Set_A_Pgm2 {
    public static void main(String args[]) {
        Scanner scn = new Scanner(System.in);
        System.out.println("How many objects");
        int n = scn.nextInt();
        Student[] e = new Student[n];
        int id;
        String name;
        String deptName;
        double salary;
        for (int i = 0; i < n; i++) {
            System.out.println("Enter id");
            id = scn.nextInt();
            System.out.println("Enter name");
            name = scn.next();
            System.out.println("Enter salary");
            salary = scn.nextFloat();
            e[i] = new Student(id, name, salary);
            System.out.println("Object created count: " + Student.displayCount());
        }
        System.out.println("Displaying info of objects created");
        for (int i = 0; i < n; i++) {
            e[i].display();
        }
        scn.close();
    }
}
