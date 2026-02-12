import java.util.*;
import java.util.Scanner;
public class Maths {
    public static void main(String[] args) {
        // math is a class
        System.out.println(Math.max(23,12));
        System.out.println(Math.min(23,12));
        System.out.println((int)(Math.random()*100));
    
    
    
    // How to take input ?
    Scanner sc = new Scanner(System.in);
    System.out.println("Input you Favourite number : ");
    int age = sc.nextInt();
 

    float money = sc.nextFloat();
    String song = sc.nextLine();
    System.out.println(age);
    
    }
    
}
