package AdvanceProgX.Assignment09;

import java.util.*;
public class Main {
     public static void main(String[] args) {

        List<Account> accounts = new ArrayList<>();

        accounts.add(new SavingsAccount("S101", "Alice", 1000, 5));
        accounts.add(new CurrentAccount("C101", "Bob", 500, 300));

        // Operations
        accounts.get(0).deposit(200);
        accounts.get(1).withdraw(600);

        // Polymorphism
        for (Account acc : accounts) {
            acc.display();
        }
    }
}
