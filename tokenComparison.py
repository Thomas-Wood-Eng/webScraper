def token_compare(input_string1, input_string2):

    tokens1 = input_string1.split()

    tokens2 = input_string2.split()

    intersection = set(tokens1).intersection(set(tokens2))
    union = set(tokens1).union(set(tokens2))
    similarity = len(intersection) / len(union)

    return similarity