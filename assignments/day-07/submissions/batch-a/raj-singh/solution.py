import csv
### Question 1: Read the CSV File
try:
    with open("sales_data.csv","r") as data:
        c=0
        read=csv.DictReader(data)       #use of inbuilt module for return in dictionary
        for line in read:
            c=c+1
        print("Total orders:",c)
except FileNotFoundError:
    print("No sales_data.csv found")


### Question 2: Total Units Sold
try:
    with open("sales_data.csv","r") as data:
        read=csv.DictReader(data)
        unit=0
        for line in read:
            unit=unit+int(line["quantity"])
        print("Total units sold:",unit)
except:
    print("File not found")



## Question 3: Total Revenue
try:
    with open("sales_data.csv","r") as data:
        read=csv.DictReader(data)
        revenue=0
        for line in read:
            revenue=revenue+int(line["quantity"])*int(line["price"])
        print("Total revenue:",revenue)
except:
    print("File not found")


## Question 4: Average Order Revenue
try:
    with open("sales_data.csv","r") as data:
        read=csv.DictReader(data)
        revenue=0
        c=0
        for line in read:
            c+=1
            revenue=revenue+int(line["quantity"])*int(line["price"])
        Average_Order_Revenue=revenue/c
        print(f"Average order revenue: {Average_Order_Revenue:.2f}")
except:
    print("File not found")


## Question 5: Category Revenue Report
try:
    with open("sales_data.csv","r") as data:
        read=csv.DictReader(data)
        revenue={}
        for sale in read:
            category=sale["category"]
            if category in ["Online Course","Workshop"]:
                if category not in revenue:
                    revenue[category]=0
                revenue[category]=revenue[category]+int(sale["price"])*int(sale["quantity"])
        print(revenue)
except:
    print("file not found")


## Question 6: City Revenue Report
try:
    with open("sales_data.csv","r") as data:
        read=csv.DictReader(data)
        revenue={}
        for sale in read:
            category=sale["city"]
            if category in ["Gorakhpur","Lucknow","Deoria"]:
                if category not in revenue:
                    revenue[category]=0
                revenue[category]=revenue[category]+int(sale["price"])*int(sale["quantity"])
        print(revenue)
except:
    print("file not found")


### Question 7: Top Product
try:
    with open("sales_data.csv","r") as data:
        read=csv.DictReader(data)
        revenue={}
        for sale in read:
            category=sale["product"]
            if category in ["Python Course","Data Analytics Course","AI Workshop"]:
                if category not in revenue:
                    revenue[category]=0
                revenue[category]=revenue[category]+int(sale["price"])*int(sale["quantity"])
        x=max(revenue.values())
        for k,v in revenue.items():
            if v==x:
                print("Top product:",k)
except:
    print("file not found")


### Question 8: Gorakhpur Orders
try:
    with open("sales_data.csv","r") as data:
        read=csv.DictReader(data)
        order=[]
        for sale in read:
            category=sale["city"]
            if category in ["Gorakhpur"]:
                order.append(sale["order_id"])
        print("Gorakhpur order IDs:",order)
except:
    print("file not found")