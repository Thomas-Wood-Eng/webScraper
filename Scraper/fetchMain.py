from fetchSafeway import fetchSafewayMain
from fetchSaveOn import fetchSaveOnMain
from fetchSuperStore import fetchSuperstoreMain
from fetchNoFrills import fetchNoFrillsMain
from fetchIGABC import fetchIGABCMain
from fetchWalmartV2 import fetch_walmartV2

from parserWalmart import walmartParser
from jsonParserIGABC import parseIGA
from jsonParserSafeway import parseSafeway
from jsonParserSuperstoreNoFrills import parseNoFrills
from jsonParserSuperstoreNoFrills import parseSuperstore

#from fuzzywuzzyCompare import compare
import os
import json

DEBUG = False

def fetchAndCompare(queries, province_id:int):
    
    for squery in queries:

        safewayResponce = fetchSafewayMain(squery)
        #fetchSaveOnMain(squery)
        superstoreResponce = fetchSuperstoreMain(squery)
        noFrillsResponce = fetchNoFrillsMain(squery)
        igaResponce = fetchIGABCMain(squery)
        walmartResponce = fetch_walmartV2(squery)

        igaList = parseIGA(igaResponce)
        noFrillsList = parseNoFrills(noFrillsResponce)
        safewayList = parseSafeway(safewayResponce)
        superstoreList = parseSuperstore(superstoreResponce)
        #saveOnList = fetchSaveOnMain(squery)
        walmartList = walmartParser(walmartResponce)

        #groupList = compare(safewayList, superstoreList, noFrillsList, igaList, walmartList, saveOnList, squery, province_id)
            
        # deleting the fetch jsons
        
        # if(not DEBUG):
        #     if(os.path.exists('fetch_IGA-BC.json')):
        #         os.remove('fetch_IGA-BC.json')
        #     if(os.path.exists('fetch_nofrills.json')):
        #         os.remove('fetch_nofrills.json')
        #     if(os.path.exists('fetch_safeway.json')):
        #         os.remove('fetch_safeway.json')
        #     if(os.path.exists('fetch_SaveOn.json')):
        #         os.remove('fetch_SaveOn.json')
        #     if(os.path.exists('fetch_superstore.json')):
        #         os.remove('fetch_superstore.json')

        

        # with open("matchedGroups.json", "w") as f:
        #     json.dump(groupList, f)
        
        print(walmartList)

    return True

if __name__ == '__main__':
    queries = [
        "White bread",
        "Eggs",
        "Milk",
        "Apples",
        "Chicken breast",
        "Spinach",
        "Cheese",
        "Ground beef",
        "Rice",
        "Tomatoes",
        "Bananas",
        "Yogurt",
        "Onions",
        "Salmon",
        "Carrots",
        "Potatoes",
        "Orange juice",
        "Strawberries",
        "Cucumber",
        "Pasta",
        "Lettuce",
        "Peanut butter",
        "Green beans",
        "Blueberries",
        "Watermelon",
        "Olive oil",
        "Almonds",
        "Grapes",
        "Avocado",
        "Cereal",
        "Broccoli",
        "Orange",
        "Lemons",
        "Honey",
        "Sliced turkey",
        "Cherries",
        "Mushrooms",
        "Bell peppers",
        "Pineapple",
        "Sausages",
        "Tofu",
        "Coconut milk",
        "Canned beans",
        "Hamburger buns",
        "Frozen peas",
        "Quinoa",
        "Greek yogurt",
        "Cottage cheese",
        "Sour cream",
        "Oatmeal",
        "Mayonnaise",
        "Salsa",
        "Parmesan cheese",
        "Bacon",
        "Cheddar cheese",
        "Ice cream",
        "Green tea",
        "Honeydew melon",
        "Dark chocolate",
        "Ground cinnamon",
        "Vanilla extract"
    ]
    province_id = 2 # temporary placeholder - add code to set this when being called
    fetchAndCompare(queries, 2)