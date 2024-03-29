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

def clean(text, word_to_remove):
    # Remove special characters using regular expressions
    cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # Remove the specified word (case-insensitive)
    cleaned_text = re.sub(fr"\b{re.escape(word_to_remove)}\b", "", cleaned_text, flags=re.IGNORECASE)
    
    cleaned_text = cleaned_text.lower()

    return cleaned_text