import java.util.*;
//import java.util.Arrays;
public class arr{
    public static void main(String[] args){
        int age =30;
        int physics =97;
        int chem =98;
        int eng = 94;

        //Array are Non Primitive
        int[] marks = new int[3];   // new only if value is assigned latter
        marks[0]=47;
        marks[1]=92;
        marks[2]=83;
        System.out.println(marks);   // This doesnot give our marks inputs
        System.out.println(marks[0]);
        System.out.println(marks[1]);
        System.out.println(marks[2]);

        //⭐ By default if marks is not initialised then, Null is Stored
        // for int default -> 0
        // for boolean default -> false
        // for otherwise default -> Null

        // methods of array are : 
        // length
        System.out.println(marks.length);

        // sorting
        Arrays.sort(marks);    // Arrays is a class which gives the sort for arr
        System.out.println(marks[0]);
        System.out.println(marks[1]);
        System.out.println(marks[2]);


        // Method 2 for array
        int[] marks2 ={ 47,90,49};

       // 2d array is given as 
    
       int[][] finalmarks = {{19,23,53},{54,43,45}};
       System.out.println(finalmarks[0][2]);
    }

    
}
