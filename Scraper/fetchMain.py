from fetchSafeway import fetchSafewayMain
from fetchSaveOn import fetchSaveOnMain
from fetchSuperStore import fetchSuperstoreMain
from fetchNoFrills import fetchNoFrillsMain
from fetchIGABC import fetchIGABCMain

from jsonParserIGABC import parseIGA
from jsonParserSafeway import parseSafeway
from jsonParserSuperstoreNoFrills import parseNoFrills
from jsonParserSuperstoreNoFrills import parseSuperstore

from fuzzywuzzyCompare import compare

query = 'bread'

fetchSafewayMain(query)
fetchSaveOnMain(query)
fetchSuperstoreMain(query)
fetchNoFrillsMain(query)
fetchIGABCMain(query)

igaList = parseIGA()
noFrillsList = parseNoFrills()
safewayList = parseSafeway()
superstoreList = parseSuperstore()

compare(safewayList, superstoreList, noFrillsList, igaList)

