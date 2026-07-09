import csv
import csv
import os

file_path = os.path.join(os.path.dirname(__file__), "sales_data.csv")
count = 0
try:
    with open(file_path, "r") as file:
        data = csv.DictReader(file)
        for row in data:
            count+=1
    print("Total orders:", count)       
except FileNotFoundError:
    print("File not found")
try:
    total_units_sold=[]
    with open(file_path, "r") as file:
        data = csv.DictReader(file)
        for row in data:
            total_units_sold.append(int(row["quantity"]))  
    print("Total units sold:", sum(total_units_sold))
except FileNotFoundError:   
    print("File not found")

try:
    total_revenue=[]
    with open(file_path,"r") as file:
        data=csv.DictReader(file)
        for row in data:
            total_revenue.append(int(row["quantity"])*int(row["price"]))
    print("Total revenue:",sum(total_revenue)) 
except FileNotFoundError:
    print("file not found")           
average_revenue=sum(total_revenue)/count
print(f"Average order revenue:",round(average_revenue,2))
try:
    dict1={"Online Course":0,
           "Workshop":0}
    with open(file_path,"r") as file:
        data=csv.DictReader(file)
        for item in data:
            if item["category"]=="Online Course":
                dict1["Online Course"]+=int(item["price"])*int(item["quantity"])
            else:
                 dict1["Workshop"]+=int(item["price"])*int(item["quantity"]) 
    print(dict1) 
except FileNotFoundError:
    print("file not found")                  

try:
    dict2={"Gorakhpur":0,
           "Lucknow":0,
           "Deoria":0}
    with open(file_path,"r") as file:
        data=csv.DictReader(file)
        for item in data:
            if item["city"]=="Gorakhpur":
                dict2["Gorakhpur"]+=int(item["price"])*int(item["quantity"])
            elif item["city"]=="Lucknow":
                 dict2["Lucknow"]+=int(item["price"])*int(item["quantity"])
            elif item["city"]=="Deoria":
                   dict2["Deoria"]+=int(item["price"])*int(item["quantity"])
            else:
                pass            
    print(dict2) 
except FileNotFoundError:
    print("file not found") 
try:
    product_revenue = {}
    with open(file_path,"r") as file:
        data= csv.DictReader(file)
        for item in data:
            product_name = item["product"]
            revenue = int(item["price"])*int(item["quantity"])
            product_revenue[product_name] = product_revenue.get(product_name, 0) + revenue
    product = max(product_revenue, key=product_revenue.get)
    print("Top product:",product)
except FileNotFoundError:
    print("file not found")
try:
   list1=[]
   with open(file_path,"r") as file:
        data= csv.DictReader(file)
        for item in data:
            if item["city"]=="Gorakhpur":
                list1.append(item["order_id"])                    
   print("Gorakhpur order IDs:", list1)
except FileNotFoundError:
    print("file not found") 