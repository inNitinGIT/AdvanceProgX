# List of products (each product is stored as a dictionary)
# product is a list and inside elements are dictionary

products = [
    {"name": "Biscuit", "stock": 15},
    {"name": "Kuch kuch", "stock": 8},
    {"name": "Mint fresh", "stock": 5},
    {"name": "Mushroom", "stock": 12},
    {"name": "DairyMilk", "stock": 3}
]

print("Products with stock less than 10:\n")

# Loop through products and check stock
for product in products:
    if product["stock"] < 10:
        print("Product Name:", product["name"])
        print("Stock Quantity:", product["stock"])
        print("----")