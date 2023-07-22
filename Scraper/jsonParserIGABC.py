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
        
        if "CountDetails" in product_data:
            if product_data["CountDetails"]["DiscountPriceText"] == None:
                price = product_data["Price"]
            else:
                price = product_data["CountDetails"]["DiscountPriceText"]
            # print(price)
            product["total_price"] = price
            
        #if "ImageURL" in product_data:
        image = product_data["ImageURL"]
        product["image_link"] = image
            
        product["merchant"] = "IGA"
        
        if "Amount" in product_data:
            unit = product_data["Amount"]
            product["unit"] = unit
            
        if "IsActive" in product_data:
            avalible = product_data["IsActive"]
            product["is_available"] = avalible
        
        product["amount"] = 1
        
        if "ProductID" in product_data:
            product["merchant_productId"] = product_data["ProductID"]
            
        product["storeID"] = ""
        
        productList.append(product)
        
    #print(productList)
    return(productList)

parseIGA()   



        