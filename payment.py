from abc import ABC, abstractmethod

# Payment interface

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Credit card payment

class CreditCardPayment(PaymentMethod):

    def pay(self, amount):

        print(f"\n[PAYMENT] ₹{amount} paid using Credit Card")


# UPI payment

class UPIPayment(PaymentMethod):

    def pay(self, amount):

        print(f"\n[PAYMENT] ₹{amount} paid using UPI")


# Wallet payment

class WalletPayment(PaymentMethod):

    def pay(self, amount):

        print(f"\n[PAYMENT] ₹{amount} paid using Wallet")