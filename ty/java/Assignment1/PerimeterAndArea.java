import java.util.Scanner;
class PerimeterAndArea{
    public static void main(String[] args) {
        Scanner scn=new Scanner(System.in);
        int length=scn.nextInt();
        int breadth=scn.nextInt();
        int area=length*breadth;
        int perimeter=2*(length+breadth);
        System.out.println("area is :"+area);
        System.out.println("perimeter is :"+perimeter);
        scn.close();
    }
} 