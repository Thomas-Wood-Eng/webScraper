from re import sub

def priceParser(priceText:str):
    parseList = priceText.split()
    price = sub(r'[^\d.]', '', parseList[0])
    return float(price)
