# Topic: CSV Data Analytics With Python

import csv

# Read all CSV records and return them as a list
def load_sales_data():
    records = []

    with open("sales_data.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
           row["price"] = int(row["price"])  # Convert price to integer
           row["quantity"] = int(row["quantity"]) # Convert quantity to integer
           records.append(row)

    return records


# Load complete dataset
sales = load_sales_data()

# (Ques 1) Count Total Orders
print("Total orders:", len(sales))

# (Ques 2) Total Units Sold
units_sold = 0
for order in sales:
    units_sold += order["quantity"]       # Add quantity from every order

print("Total units sold:", units_sold)

# (Ques 3) Total Revenue
total_revenue = 0
for order in sales:
    revenue = order["price"] * order["quantity"]     # Revenue of one order
    total_revenue += revenue
print("Total revenue:", total_revenue)

# (Ques 4) Average Order Revenue
average_revenue = total_revenue / len(sales)
print("Average order revenue:", round(average_revenue, 2))

# (Ques 5) Revenue Category Wise
category_report = {}
for order in sales:
    category = order["category"]
    revenue = order["price"] * order["quantity"]
    category_report[category] = category_report.get(category, 0) + revenue
print(category_report)

# (Ques 6) Revenue City Wise
city_report = {}
for order in sales:
    city = order["city"]
    revenue = order["price"] * order["quantity"]
    city_report[city] = city_report.get(city, 0) + revenue
print(city_report)

# (Ques 7) Top Product By Revenue
product_report = {}
for order in sales:
    product = order["product"]
    revenue = order["price"] * order["quantity"]
    product_report[product] = product_report.get(product, 0) + revenue
top_product = ""
highest_revenue = 0
for product, revenue in product_report.items():
    if revenue > highest_revenue:
        highest_revenue = revenue
        top_product = product
print("Top product:", top_product)

# (Ques 8) Gorakhpur Order IDs
gorakhpur_orders = []
for order in sales:
    if order["city"] == "Gorakhpur":
        gorakhpur_orders.append(order["order_id"])
print("Gorakhpur order IDs:", gorakhpur_orders)
