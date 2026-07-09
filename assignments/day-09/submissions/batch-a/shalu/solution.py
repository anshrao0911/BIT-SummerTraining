import pandas as pd

# Use this data to create a DataFrame:
sales_data = {
    "product": ["Python Course", "Data Analytics Course", "AI Workshop", "Python Course", "Data Analytics Course", "AI Workshop"],
    "category": ["Online Course", "Online Course", "Workshop", "Online Course", "Online Course", "Workshop"],
    "price": [999, 1499, 799, 999, 1499, 799],
    "quantity": [2, 1, 3, 1, 2, 1],
    "city": ["Gorakhpur", "Lucknow", "Gorakhpur", "Deoria", "Gorakhpur", "Lucknow"]
}
### Question 1: Create and Print a DataFrame

# Create a DataFrame named `df` from `sales_data`. Print the DataFrame.
df=pd.DataFrame(sales_data)
print(df)

### Question 2: Inspect the Data

# Print the number of rows and columns in this format:

# Expected Output:
# Rows: 6
# Columns: 5
rows,columns=df.shape
print(f"Rows: {rows}\nColumns: {columns}")

### Question 3: Add Revenue Column

# Create a `revenue` column using `price * quantity`. Print only the `product` and `revenue` columns.

df["revenue"]=df["price"]*df["quantity"]
print(df[["product","revenue"]])

### Question 4: Total Revenue

# Calculate and print the total revenue.

# Expected Output:
# Total revenue: 10690
total_revenue=df["revenue"].sum()
print("Total revenue:",total_revenue)

### Question 5: Filter Gorakhpur Sales

# Create a new DataFrame containing rows where the city is `Gorakhpur`. Print its `product`, `quantity`, and `revenue` columns.
df_gkp=df[df["city"]=="Gorakhpur"]
print(df_gkp[["product","quantity","revenue"]])

### Question 6: Revenue by Category

# Use `groupby` to calculate and print total revenue by category.

# Expected Values:
# Online Course: 7494
# Workshop: 3196
Revenue_Category=df.groupby("category")["revenue"].sum()
for category, revenue in Revenue_Category.items():
    print(f"{category}: {revenue}")

### Question 7: Revenue by City

# Use `groupby` to calculate and print total revenue by city.

# Expected Values:
# Deoria: 999
# Gorakhpur: 7393
# Lucknow: 2298
revenue_city=df.groupby("city")["revenue"].sum()
for city, revenue in revenue_city.items():
    print(f"{city}: {revenue}")

### Question 8: Top Revenue Product

# Group the data by product, find the product with the highest total revenue, and print it.

# Expected Output:
# Top product: Data Analytics Course
Product=df.groupby("product")["revenue"].sum()
Product=Product.sort_values(ascending=False).index[0]
print("Top product:",Product)
