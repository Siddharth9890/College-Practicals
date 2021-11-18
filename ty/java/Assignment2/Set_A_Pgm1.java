import java.util.Scanner;

public class Main {
    int id;
    String name;
    String deptName;
    float salary;
    static int numberOfObjects = 0;

    Main() {
        id = 0;
        name = "";
        deptName = "";
        salary = 0;
    }

    Main(int id, String name, String deptName, float salary) {

        this.id = id;
        this.name = name;
        this.deptName = deptName;
        this.salary = salary;
        numberOfObjects++;

    }

    public void display() {

        System.out.println("\nEmployee Id :" + id + "\nEmployee name: " + name + "\nEmployee deptname:" + deptName
                + "\nEmployee Salary :" + salary);

    }

    public static void main(String[] args) {

        int n = 0;
        Scanner scn = new Scanner(System.in);
        System.out.print("How many employees :");
        n = scn.nextInt();
        Main[] ob = new Main[n];
        for (int i = 0; i < n; i++) {

            scn = new Scanner(System.in);
            System.out.println("Enter Id of employee " + (i + 1) + "  :");
            int id = scn.nextInt();
            System.out.println("Enter Name of employee " + (i + 1) + "  :");
            scn.nextLine();
            String name = scn.nextLine();
            System.out.println("Enter dept name of employee " + (i + 1) + "  :");
            String deptName = scn.nextLine();
            System.out.println("Enter salary of employee " + (i + 1) + "  :");
            float salary = scn.nextFloat();
            ob[i] = new Main(id, name, deptName, salary);
            System.out.println("\nNumber of Objects : " + numberOfObjects);

        }

        for (int i = 0; i < n; i++) {
            ob[i].display();

        }
        scn.close();
    }
}