public class Static {
    public static class Employee{
        String name;
        static String companyName="tcs";
        public Employee(String name)
        {
            this.name=name;
        }
        public void display()
        {
            System.out.println(name+" "+companyName);
        }
    }
    public static void main(String[] args) {
        Employee e=new Employee("name");
        e.display();
    }
}
