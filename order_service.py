# Process orders

class OrderService:

    def __init__(self,
                 payment_method,
                 notification_service,
                 storage):

        self.payment_method = payment_method
        self.notification_service = notification_service
        self.storage = storage

    def process_order(self, order):

        amount = order.get_final_price()

        print("\n========== ORDER PROCESSING ==========")

        self.payment_method.pay(amount)

        order.status = "PURCHASED"

        self.storage.save_order(order)

        self.notification_service.send_notification(
            f"Order {order.order_id} purchased successfully!"
        )

        print("======================================")