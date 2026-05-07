# Manage orders

class OrderManager:

    def __init__(self):

        self.orders = []

    def create_order(self, order):

        self.orders.append(order)

        print(f"\n[ORDER CREATED] Order ID: {order.order_id}")

    def show_orders(self):

        print("\n========== ALL ORDERS ==========")

        for order in self.orders:
            print(order)

    def highest_price_order(self):

        highest = max(
            self.orders,
            key=lambda order: order.get_final_price()
        )

        print("\n========== HIGHEST PRICE ORDER ==========")

        print(highest)

    def purchase_summary(self):

        total_orders = len(self.orders)

        total_revenue = 0

        for order in self.orders:
            total_revenue += order.get_final_price()

        print("\n========== PURCHASE SUMMARY ==========")

        print(f"Total Orders  : {total_orders}")
        print(f"Total Revenue : ₹{total_revenue}")