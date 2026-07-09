import csv
### Question 1: Read the CSV File

# Read all rows from `sales_data.csv` and print the total number of orders.

# Expected Output:
# Total orders: 6
with open("sales_data.csv", "r") as file:
    data = csv.DictReader(file)
    total_order = 0
    
    for row in data:
        total_order += 1
        
    print(f"Total orders: {total_order}")

### Question 2: Total Units Sold

# Calculate and print the total quantity sold.

# Expected Output:
# Total units sold: 10
total_sold=0

with open("sales_data.csv","r") as file:
    data=csv.DictReader(file)

    for row in data:
        total_sold+=int(row["quantity"])

print("Total units sold:",total_sold)

### Question 3: Total Revenue

#Calculate and print the total revenue from the CSV data.

# Expected Output:
# Total revenue: 10690
revenue=0

with open("sales_data.csv","r") as file:
    data=csv.DictReader(file)

    for row in data:
        revenue+=int(row["quantity"]) *int (row["price"])

print("Total revenue:",revenue)

### Question 4: Average Order Revenue

# Calculate total revenue divided by total orders. Round the result to 2 decimal places.

# Expected Output:
# Average order revenue: 1781.67
print("Average order revenue:",round(revenue/total_order,2))

### Question 5: Category Revenue Report

# Create and print a dictionary of total revenue by category.

# Expected Output:
# {'Online Course': 7494, 'Workshop': 3196}
with open("sales_data.csv", "r") as file:
    data = csv.DictReader(file)

    category_revenue = {}

    for row in data:
        category = row["category"]
        revenue = int(row["price"]) * int(row["quantity"])

        if category not in category_revenue:
            category_revenue[category] = 0

        category_revenue[category] += revenue

print(category_revenue)

### Question 6: City Revenue Report

# Create and print a dictionary of total revenue by city.

# Expected Output:
# {'Gorakhpur': 7393, 'Lucknow': 2298, 'Deoria': 999}
with open("sales_data.csv", "r") as file:
    data = csv.DictReader(file)

    city_revenue = {}

    for row in data:
        city = row["city"]
        revenue = int(row["price"]) * int(row["quantity"])

        if city not in city_revenue:
            city_revenue[city] = 0

        city_revenue[city] += revenue

print(city_revenue)

### Question 7: Top Product

# Find the product with the highest total revenue and print it.

# Expected Output:
# Top product: Data Analytics Course
with open("sales_data.csv", "r") as file:
    data = csv.DictReader(file)
    
    product_revenue = {}
    
    for row in data:
        product = row["product"]
        row_revenue = int(row["price"]) * int(row["quantity"])
        
        if product not in product_revenue:
            product_revenue[product] = 0
            
        product_revenue[product] += row_revenue

    top_product = ""
    max_revenue = 0
    for product in product_revenue:
        if product_revenue[product] > max_revenue:
            max_revenue = product_revenue[product]
            top_product = product

print("Top product:", top_product)

### Question 8: Gorakhpur Orders

# Create a list of `order_id` values where the city is `"Gorakhpur"`. Keep the CSV order and print the list.

# Expected Output:
# Gorakhpur order IDs: ['ORD-001', 'ORD-003', 'ORD-005']

with open("sales_data.csv", "r") as file:
    data = csv.DictReader(file)
    
    gorakhpur_orders = []
    
    for row in data:
        if row["city"] == "Gorakhpur":
            gorakhpur_orders.append(row["order_id"])

print("Gorakhpur order IDs:", gorakhpur_orders)



