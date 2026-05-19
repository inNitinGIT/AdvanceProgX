from Assignment12.order import *
from Assignment12.payment import *
from Assignment12.notification import *
from Assignment12.storage import *
from Assignment12.order_service import OrderService
from Assignment12.order_manager import OrderManager
from Assignment12.products_data import products

# Main program

manager = OrderManager()

print("\n========== E-COMMERCE ORDER SYSTEM ==========")

order_id = int(input("\nEnter Order ID: "))
customer_name = input("Enter Customer Name: ")

# Order type
print("\nSelect Order Type")
print("1. Regular")
print("2. Discounted")
print("3. Priority")

choice = int(input("Enter choice: "))

if choice == 1:
    order = RegularOrder(order_id, customer_name)

elif choice == 2:
    order = DiscountedOrder(order_id, customer_name)

else:
    order = PriorityOrder(order_id, customer_name)

# Show products
print("\n========== PRODUCTS ==========")

for product in products:
    print(product)

# Add products
count = int(input("\nHow many products? "))

for i in range(count):

    product_id = int(input(f"Enter product id {i+1}: "))

    for product in products:

        if product.product_id == product_id:
            order.add_product(product)

# Create order
manager.create_order(order)

# Payment method
print("\nSelect Payment")
print("1. Credit Card")
print("2. UPI")
print("3. Wallet")

payment_choice = int(input("Enter choice: "))

if payment_choice == 1:
    payment = CreditCardPayment()

elif payment_choice == 2:
    payment = UPIPayment()

else:
    payment = WalletPayment()

# Notification
print("\nSelect Notification")
print("1. Email")
print("2. SMS")
print("3. Push")

notification_choice = int(input("Enter choice: "))

if notification_choice == 1:
    notification = EmailNotification()

elif notification_choice == 2:
    notification = SMSNotification()

else:
    notification = PushNotification()

# Storage
print("\nSelect Storage")
print("1. Database")
print("2. File")

storage_choice = int(input("Enter choice: "))

if storage_choice == 1:
    storage = DatabaseStorage()

else:
    storage = FileStorage()

# Process order
service = OrderService(
    payment,
    notification,
    storage
)

service.process_order(order)

# Results
manager.show_orders()
manager.highest_price_order()
manager.purchase_summary()