from fetchSafeway import fetchSafewayMain
from fetchSaveOn import fetchSaveOnMain
from fetchSuperStore import fetchSuperstoreMain
from fetchNoFrills import fetchNoFrillsMain
from fetchIGABC import fetchIGABCMain
from fetchWalmart import fetchWalmartMain

from jsonParserIGABC import parseIGA
from jsonParserSafeway import parseSafeway
from jsonParserSuperstoreNoFrills import parseNoFrills
from jsonParserSuperstoreNoFrills import parseSuperstore

from fuzzywuzzyCompare import compare
import os
import json

DEBUG = False

def fetchAndCompare(squery:str, province_id:int):

    fetchSafewayMain(squery)
    fetchSaveOnMain(squery)
    fetchSuperstoreMain(squery)
    fetchNoFrillsMain(squery)
    fetchIGABCMain(squery)

    igaList = parseIGA()
    noFrillsList = parseNoFrills()
    safewayList = parseSafeway()
    superstoreList = parseSuperstore()
    saveOnList = fetchSaveOnMain(squery)
    walmartList = fetchWalmartMain(squery)

    groupList = compare(safewayList, superstoreList, noFrillsList, igaList, walmartList, saveOnList, squery, province_id)
        
    # deleting the fetch jsons
    if(not DEBUG):
        if(os.path.exists('fetch_IGA-BC.json')):
            os.remove('fetch_IGA-BC.json')
        if(os.path.exists('fetch_nofrills.json')):
            os.remove('fetch_nofrills.json')
        if(os.path.exists('fetch_safeway.json')):
            os.remove('fetch_safeway.json')
        if(os.path.exists('fetch_SaveOn.json')):
            os.remove('fetch_SaveOn.json')
        if(os.path.exists('fetch_superstore.json')):
            os.remove('fetch_superstore.json')

    

    with open("matchedGroups.json", "w") as f:
        json.dump(groupList, f)

    return groupList

if __name__ == '__main__':
    query = 'milk'
    province_id = 2 # temporary placeholder - add code to set this when being called
    fetchAndCompare(query, 2)