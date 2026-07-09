# Topic : Data Analytics Fundamentals With Python

# Sales dataset provided in the assignment
sales = [
    {
        "product": "Python Course",
        "category": "Online Course",
        "price": 999,
        "quantity": 2,
        "city": "Gorakhpur",
    },
    {
        "product": "Data Analytics Course",
        "category": "Online Course",
        "price": 1499,
        "quantity": 1,
        "city": "Lucknow",
    },
    {
        "product": "AI Workshop",
        "category": "Workshop",
        "price": 799,
        "quantity": 3,
        "city": "Gorakhpur",
    },
    {
        "product": "Python Course",
        "category": "Online Course",
        "price": 999,
        "quantity": 1,
        "city": "Deoria",
    },
    {
        "product": "Data Analytics Course",
        "category": "Online Course",
        "price": 1499,
        "quantity": 2,
        "city": "Gorakhpur",
    },
    {
        "product": "AI Workshop",
        "category": "Workshop",
        "price": 799,
        "quantity": 1,
        "city": "Lucknow",
    },
]
# For each record, revenue means:
# revenue = price * quantity

# (Ques 1) Count Total Orders

total_orders = len(sales)  # Count total sales records
print("Total orders:", total_orders)

# (Ques 2) Count Total Units Sold

total_units = 0  # Variable to store total quantity
for record in sales:
    # Add quantity of every record
    total_units += record["quantity"]
print("Total units sold:", total_units)

# (Ques 3) Calculate Total Revenue

total_revenue = 0
for record in sales:
    revenue = record["price"] * record["quantity"]  # Revenue for current order
    total_revenue += revenue  # Add into overall revenue

print("Total revenue:", total_revenue)

# (Ques 4) Revenue From Gorakhpur

gorakhpur_revenue = 0
for record in sales:
    if record["city"] == "Gorakhpur":                      # Check city name
        gorakhpur_revenue += record["price"] * record["quantity"]
print("Gorakhpur revenue:", gorakhpur_revenue)

# (Ques 5) Revenue Category Wise

category_revenue = {}
for record in sales:
    category = record["category"]                           # Extract category
    revenue = record["price"] * record["quantity"]
    if category in category_revenue:
        category_revenue[category] += revenue  # Update existing category
    else:
        category_revenue[category] = revenue  # Create new category

print(category_revenue)

# (Ques 6) Revenue City Wise

city_revenue = {}
for record in sales:
    city = record["city"]                                    # Extract city
    revenue = record["price"] * record["quantity"]
    if city in city_revenue:
        city_revenue[city] += revenue  # Update city revenue
    else:
        city_revenue[city] = revenue  # Add new city

print(city_revenue)

# (Ques 7) Best Selling Product By Revenue

product_revenue = {}
for record in sales:
    product = record["product"]
    revenue = record["price"] * record["quantity"]

    if product in product_revenue:
        product_revenue[product] += revenue  # Add revenue of same product
    else:
        product_revenue[product] = revenue  # Store first revenue
highest_revenue = 0
top_product = ""
for product in product_revenue:
    if product_revenue[product] > highest_revenue:
        highest_revenue = product_revenue[product]
        top_product = product
print("Top product:", top_product)

# (Ques 8) High Volume Products

high_volume_products = []
for record in sales:
    if record["quantity"] >= 2:  # Select products with quantity 2 or more
        high_volume_products.append(record["product"])
print(high_volume_products)
