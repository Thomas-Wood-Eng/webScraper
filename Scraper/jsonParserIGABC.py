import json

def parseIGA():

    # Read the JSON file
    with open('fetch_IGA-BC.json') as f:
        data = json.load(f)
    
    productList = []

    # Iterate over the nested structure to find the "brand" value
    for product_data in data["Products"]["Result"]:
    
        product = {}
    
        if "Brand" in product_data:
            brand = product_data["Brand"]
            # print(brand)
            product["brand"] = brand
        
        
        if "Name" in product_data:
            name = product_data["Name"]
            # print(name)
            product["name"] = name
        
        if "Price" in product_data:
            price = product_data["Price"]
            print(price)
            product["price"] = price
        
        productList.append(product)
        
    return(productList)   

        