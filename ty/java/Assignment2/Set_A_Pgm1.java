import java.util.Scanner;

class Employee {
    int id;
    String name;
    String deptName;
    float salary;
    static int count;

    Employee() {
        id = 0;
        name = "";
        deptName = "";
        salary = 0;
        count++;
    }

    Employee(int id, String name, String deptName, float salary) {
        this.id = id;
        this.name = name;
        this.deptName = deptName;
        this.salary = salary;
        count++;
    }

    static int getCount() {
        return count;
    }

    public void displayInfo() {
        System.out.println("Name is : " + name);
        System.out.println("deptName is : " + deptName);
        System.out.println("salary is : " + salary);

    }
}

public class Set_A_Pgm1 {
    public static void main(String args[]) {
        Scanner scn = new Scanner(System.in);
        System.out.println("How many objects");
        int n = scn.nextInt();
        Employee[] e = new Employee[n];
        int id;
        String name;
        String deptName;
        float salary;
        for (int i = 0; i < n; i++) {
            System.out.println("Enter id");
            id = scn.nextInt();
            System.out.println("Enter name");
            name = scn.next();
            System.out.println("Enter deptName");
            deptName = scn.next();
            System.out.println("Enter salary");
            salary = scn.nextFloat();
            e[i] = new Employee(id, name, deptName, salary);
            System.out.println("Object created count: " + Employee.getCount());
        }
        System.out.println("Displaying info of objects created");
        for (int i = 0; i < n; i++) {
            e[i].displayInfo();
        }
        scn.close();
    }
}
