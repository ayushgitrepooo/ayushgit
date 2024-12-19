class Calculator {
    // Overloaded method to add two integers
    public int add(int a, int b) {
        return a + b;
    }

    // Overloaded method to add three integers
    public int add(int a, int b, int c) {
        return a + b + c;
    }

    // Overloaded method to add two doubles
    public double add(double a, double b) {
        return a + b;
    }
}

public class polymorphism {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();

        // Calls the add method with two integers
        System.out.println(calculator.add(10, 20)); // Output: 30

        // Calls the add method with three integers
        System.out.println(calculator.add(10, 20, 30)); // Output: 60

        // Calls the add method with two doubles
        System.out.println(calculator.add(10.5, 20.5)); // Output: 31.0
    }
}
