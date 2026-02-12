import java.util.*;

public class Bookfinder {

    public static void main(String[] args) {

        ArrayList<String> books = new ArrayList<>();

        books.add("Ramayana");
        books.add("Footprint without foots");
        books.add("Advance programming");
        books.add("My sql java");
        books.add("Introduction to Algorithms");

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a word to search in book titles: ");
        String searchWord = scanner.nextLine().toLowerCase();

        System.out.println("\nBooks containing \"" + searchWord + "\":");

        boolean found = false;
        // Comphresion used of searching book from log
        for (String book : books) {
            if (book.toLowerCase().contains(searchWord)) {  // more convinent 
                System.out.println(book);
                found = true;
            }
        }
        if (!found) {
            System.out.println("No books found with that word.");
        }

        scanner.close();
    }
}
