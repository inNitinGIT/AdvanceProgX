


// Note:  Strings are by default IMMUTABLE 


// Reference type or non primitive types: 
//When group of all letters/words are made are called reference or non-primitive:
public class Reference{
    public static void main(String[] args) {
        //Non primitive: 

        // this have their own functions eg string

        String name = "Nitin Roy";
        System.out.println(name);
        String friend = new String("Astitva");
        System.out.println(name.length()); // here spacing does not counted in the space
        System.out.println(friend.length());


        // String common method

        //  1}concatenate
        String name1 ="Nitin";
        String name2 ="Roy";
        String name3 = name1+" " +name2;
        System.out.println(name3);

        // 2} charAt - index accessing
        String name4 ="HanumanChalisa";
        System.out.println(name4.charAt(3));

        // 3} replace - change existing value their
        
        String name5=name4;
        name5 = name4.replace("Hanuman","Durga");
        System.out.println(name5);


        //4} substring 
        String name6 ="Nitin and monu";
        System.out.println(name6);
        System.out.println(name6.substring(0,7));
        
    }
}