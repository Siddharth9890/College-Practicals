import java.util.Scanner;

public class Employee {
    String name;
    int age;
    int salary;

    Employee(String name,int age,int salary)
    {
        this.name=name;
        this.age=age;
        this.salary=salary;
    }

    public void display()
    {
        System.out.println(name+age+salary);
    }
    public static void main(String args[])
    {
        Scanner scn=new Scanner(System.in);
        String name=scn.next();
        int age=scn.nextInt();
        int salary=scn.nextInt();
        Employee e=new Employee(name, age, salary);
        e.display();
    }
}
