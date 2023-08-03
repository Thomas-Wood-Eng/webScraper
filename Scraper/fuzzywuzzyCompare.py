from fuzzywuzzy import fuzz
import cv2
import requests
from io import BytesIO
import numpy as np
from imageCompare import compare_images
from utils import clean

def compare(safewayList, superstoreList, noFrillsList, igaList, walmartList, saveOnList, query, province_id, DEBUG=False):    

    groups = []
    groupID = 1
    
    groceryList = [safewayList, superstoreList, noFrillsList, igaList, walmartList, saveOnList]

    for itemList in groceryList:
        
        for item in itemList:
            
            igaMax = 0
            igaProduct = ""
            igaBrand = ""
            
            safewayMax = 0
            safewayProduct = ""
            safewayBrand = ""
            
            walmartMax = 0
            walmartProduct = ""
            walmartBrand = ""
            
            saveOnMax = 0
            saveOnProduct = ""
            saveOnBrand = ""
            
            noFrillsMax = 0
            noFrillsProduct = ""
            noFrillsBrand = ""
            
            superstoreMax = 0
            superstoreProduct = ""
            superstoreBrand = ""
        
            for safeway in safewayList:
                if item["merchant"].lower() == "safeway":
                    break
                
                if safeway["brand"] != None and item["brand"] != None:
                    
                    #print(compare_images(image1, image2))
                    
                    if fuzz.ratio(safeway["brand"].lower(), item["brand"].lower()) > 80:
                        similarity_ratio = fuzz.ratio(clean(safeway["name"], safeway["brand"]), clean(item["name"], item["brand"]))
                        # url = item["image_link"]
                        # if url != None:
                        #     response = requests.get(url)
                        #     image_data = BytesIO(response.content)
                            
                        #     image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                        #     image1 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                            
                        # url = safeway["image_link"]
                        # if url != None:
                        #     response = requests.get(url)
                        #     image_data = BytesIO(response.content)
                            
                        #     image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                        #     image2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                            
                        # imageComparison = compare_images(image1, image2)
                        if similarity_ratio > igaMax:                         
                            safewayMax = similarity_ratio
                            safewayProduct = safeway["name"]
                            safewayBrand = safeway["brand"]
                            safewayItem = safeway
            
            for iga in igaList:
                
                if item["merchant"].lower() == "iga":
                    break
                if iga["brand"] != None and item["brand"] != None:
                
                    if fuzz.ratio(iga["brand"].lower(), item["brand"].lower()) > 80:
                        similarity_ratio = fuzz.ratio(clean(iga["name"], iga["brand"]), clean(item["name"], item["brand"]))
                        # url = item["image_link"]
                        # if url != None:
                        #     response = requests.get(url)
                        #     image_data = BytesIO(response.content)
                            
                        #     image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                        #     image1 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                            
                        # url = iga["image_link"]
                        # if url != None:
                        #     response = requests.get(url)
                        #     image_data = BytesIO(response.content)
                            
                        #     image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                        #     image2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                            
                        # imageComparison = compare_images(image1, image2)
                        if similarity_ratio > igaMax:
                            igaMax = similarity_ratio
                            igaProduct = iga["name"]
                            igaBrand = iga["brand"]
                            igaItem = iga
            
            for noFrills in noFrillsList:
                
                if item["merchant"].lower() == "nofrills":
                    break
                
                if noFrills["brand"] != None and item["brand"] != None:
                
                    if noFrills["brand"] != None and item["brand"] != None:
                        if fuzz.ratio(noFrills["brand"].lower(), item["brand"].lower()) > 80:
                            similarity_ratio = fuzz.ratio(clean(noFrills["name"], noFrills["brand"]), clean(item["name"], item["brand"]))
                            # url = item["image_link"]
                            # if url != None:
                            #     response = requests.get(url)
                            #     image_data = BytesIO(response.content)
                                
                            #     image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                            #     image1 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            # url = noFrills["image_link"]
                            # if url != None:
                            #     response = requests.get(url)
                            #     image_data = BytesIO(response.content)
                                
                            #     image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                            #     image2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            # imageComparison = compare_images(image1, image2)
                            if similarity_ratio > noFrillsMax:
                                noFrillsMax = similarity_ratio
                                noFrillsProduct = noFrills["name"]
                                noFrillsBrand = noFrills["brand"]
                                noFrillsItem = noFrills

            for superstore in superstoreList:
                
                if item["merchant"].lower() == "superstore":
                    break
                
                if superstore["brand"] != None and item["brand"] != None:

                    if superstore["brand"] != None and item["brand"] != None:
                        if fuzz.ratio(superstore["brand"].lower(), item["brand"].lower()) > 80:
                            similarity_ratio = fuzz.ratio(clean(superstore["name"], superstore["brand"]), clean(item["name"], item["brand"]))
                            # url = item["image_link"]
                            # if url != None:
                            #     response = requests.get(url)
                            #     image_data = BytesIO(response.content)
                                
                            #     image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                            #     image1 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            # url = superstore["image_link"]
                            # if url != None:
                            #     response = requests.get(url)
                            #     image_data = BytesIO(response.content)
                                
                            #     image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                            #     image2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            # imageComparison = compare_images(image1, image2)
                            if similarity_ratio > superstoreMax:
                                superstoreMax = similarity_ratio
                                superstoreProduct = superstore["name"]
                                superstoreBrand = superstore["brand"]
                                superstoreItem = superstore
            
            for walmart in walmartList:
                
                if item["merchant"].lower() == "walmart":
                    break
                
                if walmart["brand"] != None and item["brand"] != None:
                
                    if walmart["brand"] != None and item["brand"] != None:
                        if fuzz.ratio(walmart["brand"].lower(), item["brand"].lower()) > 80:
                            similarity_ratio = fuzz.ratio(clean(walmart["name"], walmart["brand"]), clean(item["name"], item["brand"]))
                            # url = item["image_link"]
                            # if url != None:
                            #     response = requests.get(url)
                            #     image_data = BytesIO(response.content)
                                
                            #     image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                            #     image1 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            # url = walmart["image_link"]
                            # if url != None:
                            #     response = requests.get(url)
                            #     image_data = BytesIO(response.content)
                                
                            #     image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                            #     image2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            # imageComparison = compare_images(image1, image2)
                            if similarity_ratio > walmartMax:
                                walmartMax = similarity_ratio
                                walmartProduct = walmart["name"]
                                walmartBrand = walmart["brand"]
                                walmartItem = walmart
                            
            for saveOn in saveOnList:
                
                if item["merchant"] == "Save-On-Foods":
                    break
                
                if saveOn["brand"] != None and item["brand"] != None:
                
                    if saveOn["brand"] != None and item["brand"] != None:
                        if fuzz.ratio(saveOn["brand"].lower(), item["brand"].lower()) > 80:
                            similarity_ratio = fuzz.ratio(clean(saveOn["name"], saveOn["brand"]), clean(item["name"], item["brand"]))
                            # url = item["image_link"]
                            # if url != None:
                            #     response = requests.get(url)
                            #     image_data = BytesIO(response.content)
                                
                            #     image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                            #     image1 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            # url = saveOn["image_link"]
                            # if url != None:
                            #     response = requests.get(url)
                            #     image_data = BytesIO(response.content)
                                
                            #     image_np = np.asarray(bytearray(image_data.read()), dtype=np.uint8)
                            #     image2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
                                
                            # imageComparison = compare_images(image1, image2)
                            if similarity_ratio > saveOnMax:
                                saveOnMax = similarity_ratio
                                saveOnProduct = saveOn["name"]
                                saveOnBrand = saveOn["brand"]
                                saveOnItem = saveOn
            
            group = {}
            
            products = []
            
            if safewayMax >= 60:
                products.append(safeway)
            
            if igaMax >= 60:
                products.append(igaItem)
                
            if noFrillsMax >= 60:
                products.append(noFrillsItem)
                
            if superstoreMax >= 60:
                products.append(superstoreItem)
                
            if walmartMax >= 60:
                products.append(walmartItem)
                
            if saveOnMax >= 60:
                products.append(saveOnItem)
                
            group["groupID"] = groupID
            #group["search_string"] = query
            group["products"] = products
            
            if len(group["products"]) >= 1:
            
                groups.append(group)
            
                groupID += 1
    
    groupList = {
        'search_query' : query,
        'province_id' : province_id,
        'groups' : groups
    }

    if(DEBUG):
        print(groupList)
    return groupList


