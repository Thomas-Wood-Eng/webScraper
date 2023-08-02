import re

def priceParser(priceText:str):
    parseList = priceText.split()
    price = re.sub(r'[^\d.]', '', parseList[0])
    return float(price)

# source : chatGPT 3 
def extract_decimal_value(input_string):
        # Use a regular expression to extract the decimal value from the input string
        decimal_pattern = r'(\d+(\.\d+)?)'
        matches = re.findall(decimal_pattern, input_string)

        # Extract the first match (decimal value) from the list and convert it to a float
        if matches:
            decimal_value = float(matches[0][0])
            return decimal_value
        else:
            # If no decimal value is found, return None or raise an exception
            return None
