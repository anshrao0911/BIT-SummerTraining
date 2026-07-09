sales = [
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 2, "city": "Gorakhpur"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 1, "city": "Lucknow"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 3, "city": "Gorakhpur"},
    {"product": "Python Course", "category": "Online Course", "price": 999, "quantity": 1, "city": "Deoria"},
    {"product": "Data Analytics Course", "category": "Online Course", "price": 1499, "quantity": 2, "city": "Gorakhpur"},
    {"product": "AI Workshop", "category": "Workshop", "price": 799, "quantity": 1, "city": "Lucknow"},
]

### Question 1: Count Orders

print("Total orders:", len(sales))   #printing the sales 



### Question 2: Count Units Sold
quantity=0
for sale in sales:     #itrating the sales list
    quantity = quantity+sale["quantity"]       #calculating quantity of sold unit
print("Total units sold:",quantity)



### Question 3: Calculate Total Revenue
revenues = []
for sale in sales:
    revenues.append(sale["price"]*sale["quantity"])
print("Total revenue:",sum(revenues))


### Question 4: Filter Sales by City

revenues = []
for sale in sales:
    if sale["city"] == "Gorakhpur":          #comparing city by Gorakhpur
        revenues.append(sale["price"]*sale["quantity"]) #appending the value to the revenue list
print("Gorakhpur revenue:",sum(revenues))     #printing the revenue



### Question 5: Revenue by Category

revenues = {}
for sale in sales:
    category = sale["category"]
    if category in ["Online Course", "Workshop"]:
        if category not in revenues:               #checking the cotegory is in the revenue dict or not
            revenues[category] = 0
        revenues[category] =revenues[category]+ sale["price"] * sale["quantity"]
print(revenues)


### Question 6: Revenue by City

revenues = {}
for sale in sales:
    category = sale["city"]
    if category in ["Gorakhpur", "Deoria","Lucknow"]:
        if category not in revenues:               #checking the cotegory is in the revenue dict or not
            revenues[category] = 0
        revenues[category] =revenues[category]+ sale["price"] * sale["quantity"]
print(revenues)



### Question 7: Best-Selling Product by Revenue
revenues = {}
for sale in sales:
    category = sale["product"]
    if category in ["Python Course", "Data Analytics Course","AI Workshop"]:
        if category not in revenues:               #checking the cotegory is in the revenue dict or not
            revenues[category] = 0
        revenues[category] =revenues[category]+ sale["price"] * sale["quantity"]
x=max(revenues.values())     #storing the maximum value to the variable x
for k,v in revenues.items():
    if v==x:                #comparing the values to x
        print("Top product:",k)   #printing onlu key of maximum value



### Question 8: High-Volume Products

product = []
for sale in sales:
    if sale["quantity"]>=2:          #comparing quantity by greater or equal to 2
        product.append(sale["product"]) #appending the product name to the product list
print(product)