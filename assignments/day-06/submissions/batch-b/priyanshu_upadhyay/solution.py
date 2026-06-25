# Day 6 Assignment - Data Analytics Fundamentals With Python

sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]

# Question 1: Count Orders

print("Total orders:", len(sales))


# Question 2: Count Units Sold

total_units = 0

for record in sales:
    total_units += record["quantity"]

print("Total units sold:", total_units)


# Question 3: Calculate Total Revenue

total_revenue = 0

for record in sales:
    revenue = record["price"] * record["quantity"]
    total_revenue += revenue

print("Total revenue:", total_revenue)


# Question 4: Filter Sales by City

gorakhpur_revenue = 0

for record in sales:
    if record["city"] == "Gorakhpur":
        gorakhpur_revenue += record["price"] * record["quantity"]

print("Gorakhpur revenue:", gorakhpur_revenue)


# Question 5: Revenue by Category

category_revenue = {}

for record in sales:
    category = record["category"]
    revenue = record["price"] * record["quantity"]

    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print(category_revenue)


# Question 6: Revenue by City

city_revenue = {}

for record in sales:
    city = record["city"]
    revenue = record["price"] * record["quantity"]

    if city in city_revenue:
        city_revenue[city] += revenue
    else:
        city_revenue[city] = revenue

print(city_revenue)


# Question 7: Best-Selling Product by Revenue

product_revenue = {}

for record in sales:
    product = record["product"]
    revenue = record["price"] * record["quantity"]

    if product in product_revenue:
        product_revenue[product] += revenue
    else:
        product_revenue[product] = revenue

top_product = max(product_revenue, key=product_revenue.get)

print("Top product:", top_product)


# Question 8: High-Volume Products

high_volume_products = []

for record in sales:
    if record["quantity"] >= 2:
        high_volume_products.append(record["product"])

print(high_volume_products)