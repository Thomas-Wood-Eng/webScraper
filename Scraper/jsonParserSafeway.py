import json
import re

def parseSafeway():

    # Read the JSON file    
    with open('fetch_safeway.json') as f:
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
            product["total_price"] = price
            
            unit_price = product_data["price"]["unit"]["current"]["amount"]
            product["unit_price"] = unit_price
            
            """label = product_data["price"]["unit"]["label"]
            match = re.search(r"\d+(\D+)", label)
            letters = re.sub(" \d+", " ", match.group(1))
            product["unit"] = letters"""
            
            size = {}

            #label = product_data["price"]["unit"]["label"]
            #match = re.search(r"\d+(\D+)", label)

            #if match:
                #letters = re.sub(r" \d+", " ", match.group(1))
            #    size["unit"] = match.group(1)
            #else:
            #    size["unit"] = ""
            
        if "isInCurrentCatalog" in product_data:
            available = product_data["isInCurrentCatalog"]
            product["is_available"] = available
            
        if "image" in product_data:
            img = product_data["image"]["src"]
            product["image_link"] = img
            
        if "size" in product_data:
            sizeData = product_data["size"]["value"]
            size["amount"] = sizeData
            size["unit"] =  re.sub(r'[^a-zA-Z\s]', '', sizeData)
            
        product["merchant"] = "Safeway"
        
        product["storeID"] = ""
        
        product["size"] = size
        
        if "productId" in product_data:
            product["merchant_productId"] = product_data["productId"]
        
        productList.append(product)
        
    #print(productList)   
    return(productList)

if __name__ == '__main__':
    parseSafeway()
        
        
# TODO: Size conversation



