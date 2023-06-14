from superstore import superstore_main
from saveOnFoods import saveOnFoods_main
from safeway import safeway_main
from noFrills import noFrills_main
import json
import re


def scrapePrices():
    item = 'White bread'

    superstoreItems = superstore_main(item)
    saveOnFoodsItems = saveOnFoods_main(item)
    safewayItems = safeway_main(item)
    noFrillsItems = noFrills_main(item)

    for item in superstoreItems:
        if "Name" in item:
            # Add a space before a capital letter or a number
            item["Name"] = re.sub(r'(?<=[a-zA-Z])(?=[A-Z])|(?<=[a-zA-Z])(?=\d)', ' ', item["Name"])

    for item in saveOnFoodsItems:
        if "Name" in item:
            # Add a space before a capital letter or a number
            item["Name"] = re.sub(r'(?<=[a-zA-Z])(?=[A-Z])|(?<=[a-zA-Z])(?=\d)', ' ', item["Name"])

    for item in safewayItems:
        if "Name" in item:
            # Add a space before a capital letter or a number
            item["Name"] = re.sub(r'(?<=[a-zA-Z])(?=[A-Z])|(?<=[a-zA-Z])(?=\d)', ' ', item["Name"])

    for item in noFrillsItems:
        if "Name" in item:
            # Add a space before a capital letter or a number
            item["Name"] = re.sub(r'(?<=[a-zA-Z])(?=[A-Z])|(?<=[a-zA-Z])(?=\d)', ' ', item["Name"])

    itemsDict = {
        'superstore' : superstoreItems,
        'saveOnFoods' : saveOnFoodsItems,
        'safeway' : safewayItems,
        'noFrills' : noFrillsItems
    }

    with open("sample.json", "w") as outfile:
        json.dump(itemsDict, outfile)


scrapePrices()
