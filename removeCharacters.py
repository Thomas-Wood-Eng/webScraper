import re


def remove_special_characters(input_string):
    # Regular expression pattern to match special characters (excluding spaces)
    pattern = r'[^a-zA-Z0-9\s]'

    # Remove special characters using the pattern
    cleaned_string = re.sub(pattern, '', input_string)

    return cleaned_string
