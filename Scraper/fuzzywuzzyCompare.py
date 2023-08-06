from fuzzywuzzy import fuzz
import cv2
import requests
from io import BytesIO
import numpy as np
from imageCompare import compare_images
from utils import clean



def check_matches(ref_product:dict, target_productList:list):
    # find and return matching product from the store and pop from the list
    max_score = 60
    for index, target_product in enumerate(target_productList):
        if(ref_product['brand'] != None and target_product['brand'] != None):
            if fuzz.ratio(ref_product["brand"].lower(), target_product["brand"].lower()) > 80:
                similarity_ratio = fuzz.ratio(clean(ref_product["name"], ref_product["brand"]), clean(target_product["name"], target_product["brand"]))
                if similarity_ratio > max_score:                         
                    max_score = similarity_ratio
                    target_productList.pop(index)
                    return target_product



def compare(safewayList, superstoreList, noFrillsList, igaList, walmartList, saveOnList, query, province_id, DEBUG=False):    
    groceryList = [safewayList, superstoreList, noFrillsList, igaList, walmartList, saveOnList]
    groups = []
    groupID = 0

    for index, list in enumerate(groceryList):
        if(index == len(groceryList) - 1):
            break
        groceryList.pop(index)
        for item in list:
            group_products = []
            for store_list in groceryList: 
                # find a matching product from each store and append to product list
                match_from_store = check_matches(item, store_list)
                if(match_from_store is not None):
                    group_products.append(match_from_store)

            if (len(group_products)):
                curr_group = {
                    'groupID' : groupID,
                    'products' : group_products
                }
                groups.append(curr_group)
                groupID += 1
    
    groupList = {
        'search_query' : query,
        'province_id' : province_id,
        'groups' : groups
        }

    if(DEBUG):
        print(groupList)
    return groupList
