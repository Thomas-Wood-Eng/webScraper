def token_compare(input_string1:list[str], input_string2:list[str]):

    tokens1 = input_string1

    tokens2 = input_string2

    intersection = set(tokens1).intersection(set(tokens2))
    union = set(tokens1).union(set(tokens2))
    similarity = len(intersection) / len(union)

    return similarity
