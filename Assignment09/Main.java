package AdvanceProgX.Assignment09;

import java.util.*;

public class Main {
    public static void main(String[] args) {

        List<Account> accounts = new ArrayList<>();

        // Add accounts
        accounts.add(new SavingsAccount("S101", "Alice", 1000, 5));
        accounts.add(new CurrentAccount("C101", "Bob", 500, 300));
        accounts.add(new SavingsAccount("S102", "Charlie", 2000, 4));
        accounts.add(new CurrentAccount("C102", "David", 800, 400));

        // Operations
        accounts.get(0).deposit(200); // Alice → 1200
        accounts.get(1).withdraw(600); // Bob → -100 (overdraft)
        accounts.get(2).withdraw(500); // Charlie → 1500
        accounts.get(3).deposit(300); // David → 1100

        // Transfer example
        try {
            transfer(accounts.get(0), accounts.get(2), 300); // Alice → Charlie
        } catch (Exception e) {
            System.out.println("Transfer Error: " + e.getMessage());
        }

        // Invalid operation (testing validation)
        try {
            accounts.get(2).withdraw(10000); // should fail
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        // Polymorphism + subtype behavior
        for (Account acc : accounts) {

            // Extra behavior for SavingsAccount
            if (acc instanceof SavingsAccount) {
                SavingsAccount sa = (SavingsAccount) acc;
                System.out.println("Interest Earned: " + sa.calculateInterest());
            }

            acc.display(); // dynamic binding
        }
    }

    public static void transfer(Account from, Account to, double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Transfer must be positive!");
        }

        from.withdraw(amount);
        to.deposit(amount);
    }
}
