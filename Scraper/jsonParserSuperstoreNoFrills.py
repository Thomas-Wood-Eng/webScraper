import json

# Read the JSON file
with open('fetch_nofrills.json') as f:
    data = json.load(f)
    
productList = []

# Iterate over the nested structure to find the "brand" value
for product_data in data["results"]:
    
    product = {}
    
    if "brand" in product_data:
        brand = product_data["brand"]
        # print(brand)
        product["brand"] = brand
        
        
    if "name" in product_data:
        name = product_data["name"]
        # print(name)
        product["name"] = name
        
    if "prices" in product_data:
        price = product_data["prices"]["price"]["value"]
        print(price)
        product["price"] = price
        
    productList.append(product)
    
print(productList)
        