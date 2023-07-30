from fuzzywuzzy import fuzz

def compare(safewayList, superstoreList, noFrillsList, igaList, walmartList, saveOnList, query, DEBUG=False):    

    groupList = []
    groupID = 1

    for safeway in safewayList:
        igaMax = 0
        igaProduct = ""
        igaBrand = ""
        
        noFrillsMax = 0
        noFrillsProduct = ""
        noFrillsBrand = ""
        
        superstoreMax = 0
        superstoreProduct = ""
        superstoreBrand = ""
        
        walmartMax = 0
        walmartProduct = ""
        walmartBrand = ""
        
        saveOnMax = 0
        saveOnProduct = ""
        saveOnBrand = ""
        
        for iga in igaList:
            
            if iga["brand"] != None and safeway["brand"] != None and iga["name"] != None and safeway["name"] != None:
                if fuzz.ratio(iga["brand"].lower(), safeway["brand"].lower()) > 80:
                    similarity_ratio = fuzz.ratio(iga["name"], safeway["name"])
                    if similarity_ratio > igaMax:
                        igaMax = similarity_ratio
                        igaProduct = iga["name"]
                        igaBrand = iga["brand"]
                        igaItem = iga

        #print(f"Safeway Product: {safeway}")
        #print(f"IGA Product: {igaProduct}")
        #print(f"IGA Brand: {igaBrand}")
        #print(f"Similarity Ratio: {igaMax}")
        
        for noFrills in noFrillsList:
            
            if noFrills["brand"] != None and safeway["brand"] != None:
                if fuzz.ratio(noFrills["brand"].lower(), safeway["brand"].lower()) > 80:
                    similarity_ratio = fuzz.ratio(noFrills["name"], safeway["name"])
                    if similarity_ratio > noFrillsMax:
                        noFrillsMax = similarity_ratio
                        noFrillsProduct = noFrills["name"]
                        noFrillsBrand = noFrills["brand"]
                        noFrillsItem = noFrills

        #print(f"Safeway Product: {safeway}")
        #print(f"NoFrills Product: {noFrillsProduct}")
        #print(f"NoFrills Brand: {noFrillsBrand}")
        #print(f"Similarity Ratio: {noFrillsMax}")
        
        for superstore in superstoreList:
            
            if superstore["brand"] != None and safeway["brand"] != None:
                if fuzz.ratio(superstore["brand"].lower(), safeway["brand"].lower()) > 80:
                    similarity_ratio = fuzz.ratio(superstore["name"], safeway["name"])
                    if similarity_ratio > superstoreMax:
                        superstoreMax = similarity_ratio
                        superstoreProduct = superstore["name"]
                        superstoreBrand = superstore["brand"]
                        superstoreItem = superstore

        #print(f"Safeway Product: {safeway}")
        #print(f"Superstore Product: {superstoreProduct}")
        #print(f"Superstore Brand: {superstoreBrand}")
        #print(f"Similarity Ratio: {superstoreMax}")
        
        for walmart in walmartList:
            
            if walmart["brand"] != None and safeway["brand"] != None:
                if fuzz.ratio(walmart["brand"].lower(), safeway["brand"].lower()) > 80:
                    similarity_ratio = fuzz.ratio(walmart["name"], safeway["name"])
                    if similarity_ratio > walmartMax:
                        walmartMax = similarity_ratio
                        walmartProduct = walmart["name"]
                        walmartBrand = walmart["brand"]
                        walmartItem = walmart
                        
        for saveOn in saveOnList:
            
            if saveOn["brand"] != None and safeway["brand"] != None:
                if fuzz.ratio(saveOn["brand"].lower(), safeway["brand"].lower()) > 80:
                    similarity_ratio = fuzz.ratio(saveOn["name"], safeway["name"])
                    if similarity_ratio > saveOnMax:
                        saveOnMax = similarity_ratio
                        saveOnProduct = saveOn["name"]
                        saveOnBrand = saveOn["brand"]
                        saveOnItem = saveOn
        
        group = {}
        
        products = []
        
        products.append(safeway)
        
        if igaMax >= 50:
            products.append(igaItem)
            
        if noFrillsMax >= 50:
            products.append(noFrillsItem)
            
        if superstoreMax >= 50:
            products.append(superstoreItem)
            
        if walmartMax >= 50:
            products.append(walmartItem)
            
        if saveOnMax >= 50:
            products.append(saveOnItem)
            
        group["groupID"] = groupID
        group["search_string"] = query
        group["products"] = products
        
        groupList.append(group)
        
        groupID += 1
    
    if(DEBUG):
        print(groupList)
    return groupList
