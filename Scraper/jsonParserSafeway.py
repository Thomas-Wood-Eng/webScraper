import json

def parseSafeway():

    # Read the JSON file    
    with open('fetch_safeway2.json') as f:
        data = json.load(f)
    
    productList = []

    # Iterate over the nested structure to find the "brand" value
    for product_id, product_data in data["entities"]["product"].items():

        product = {}
    
        if "brand" in product_data:
            brand = product_data["brand"]
            # print(brand)
            product["brand"] = brand
        
        
        if "name" in product_data:
            name = product_data["name"]
            # print(name)
            product["name"] = name
        
        if "price" in product_data:
            price = product_data["price"]["current"]["amount"]
            # print(price)
            product["price"] = price
        
        productList.append(product)
    
    return(productList)
        