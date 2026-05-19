from abc import ABC, abstractmethod

# Base order class

class Order(ABC):

    def __init__(self, order_id, customer_name):

        self.order_id = order_id
        self.customer_name = customer_name
        self.products = []
        self.status = "CREATED"

    def add_product(self, product):

        self.products.append(product)

    def calculate_price(self):

        total = 0

        for product in self.products:
            total += product.price

        return total

    @abstractmethod
    def get_final_price(self):
        pass

    def __str__(self):

        product_names = []

        for product in self.products:
            product_names.append(product.name)

        return (
            f"\nOrder ID      : {self.order_id}"
            f"\nCustomer Name : {self.customer_name}"
            f"\nProducts      : {product_names}"
            f"\nFinal Price   : ₹{self.get_final_price()}"
            f"\nStatus        : {self.status}"
        )


# Regular order

class RegularOrder(Order):

    def get_final_price(self):

        return self.calculate_price()


# Discount order

class DiscountedOrder(Order):

    def get_final_price(self):

        total = self.calculate_price()

        return total - (total * 0.10)


# Priority order

class PriorityOrder(Order):

    def get_final_price(self):

        total = self.calculate_price()

        return total + 100