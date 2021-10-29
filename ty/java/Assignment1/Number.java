public class Number {
    public static class MyNumber {
        private int number;

        MyNumber() {
            number = 0;
        }

        MyNumber(int number) {
            this.number = number;
        }

        public void isNegative(int number) {
            boolean result = (number < 0) ? true : false;
            if (result)
                System.out.println(number + " is negative");
            else
                System.out.println(number + " is not negative");
        }

        public void isPositive(int number) {
            boolean result = (number > 0) ? true : false;
            if (result)
                System.out.println(number + " is positive");
            else
                System.out.println(number + " is not positive");
        }

        public void isZero(int number) {
            boolean result = (number == 0) ? true : false;
            if (result)
                System.out.println(number + " is zero");
            else
                System.out.println(number + " is not zero");
        }

        public void isOdd(int number) {
            boolean result = (number % 2 != 0) ? true : false;
            if (result)
                System.out.println(number + " is odd");
            else
                System.out.println(number + " is not odd");
        }

        public void isEven(int number) {
            boolean result = (number % 2 == 0) ? true : false;
            if (result)
                System.out.println(number + " is even");
            else
                System.out.println(number + " is not even");
        }

    }

    public static void main(String[] args) {
        int value = Integer.parseInt(args[0]);
        MyNumber mn = new MyNumber(value);
        mn.isNegative(value);
        mn.isPositive(value);
        mn.isZero(value);
        mn.isOdd(value);
        mn.isEven(value);

    }
}
