import json

def parseNoFrills(data):
    # Read the JSON file
    # with open('fetch_nofrills.json') as f:
    #     data = json.load(f)

    return(loblaws(data))
    
    
        
def parseSuperstore(data):
    # Read the JSON file
    # with open('fetch_superstore.json') as f:
    #     data = json.load(f)
    return(loblaws(data))
        
def loblaws(data):
    
    productList = []

    # Iterate over the nested structure to find the "brand" value
    for product_data in data["results"]:
    
        product = {}
        
        size = {}
    
        if "brand" in product_data:
            brand = product_data["brand"]
            product["brand"] = brand
        
        if "name" in product_data:
            name = product_data["name"]
            product["name"] = name
        
        if "prices" in product_data:
            price = product_data["prices"]["price"]["value"]
            product["total_price"] = price
            
            
            #unit_price = product_data["prices"]["comparisonPrices"][0]["value"]
            #product["unit_price"] = unit_price
            
            #unit = product_data["prices"]["comparisonPrices"][0]["unit"]
            
        if "packageSize" in product_data:
            packageSize = product_data["packageSize"]
            size["amount"] = packageSize
            size["unit"] = packageSize.split()[1]

            
            
        if "shoppable" in product_data:
            is_avalible = product_data["shoppable"]
            product["is_avalible"] = is_avalible
            
        if "sellerName" in product_data:
            seller = product_data["sellerName"]
            product["merchant"] = seller
            
        if "articleNumber" in product_data:
            productId = product_data["articleNumber"]
            product["merchant_productId"] = productId
            
        if "imageAssets" in product_data:
            image = product_data["imageAssets"][0]["largeRetinaUrl"]
            product["image_link"] = image
            
        product["storeID"] = ""
        
        product["size"] = size
            
        productList.append(product)
    
    #print(productList)
    return(productList)

if __name__ == '__main__':
    parseSuperstore()
    parseNoFrills()

# TODO: Find the store ID/Area the store is
        