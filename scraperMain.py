from superstore import superstore_main
from saveOnFoods import saveOnFoods_main
from safeway import safeway_main
from noFrills import noFrills_main
import json



def scrapePrices():
    item = 'White bread'

    superstoreItems = superstore_main(item)
    saveOnFoodsItems = saveOnFoods_main(item)
    safewayItems = safeway_main(item)
    noFrillsItems = noFrills_main(item)

    itemsDict = {
        'superstore' : superstoreItems,
        'saveOnFoods' : saveOnFoodsItems,
        'safeway' : safewayItems,
        'noFrills' : noFrillsItems
    }

    with open("sample.json", "w") as outfile:
        json.dump(itemsDict, outfile)


scrapePrices()




