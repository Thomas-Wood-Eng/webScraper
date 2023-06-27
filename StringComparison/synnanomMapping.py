from nltk.corpus import wordnet
import nltk

def are_synonymous(string1:list[str], string2:list[str]):
    nltk.download('wordnet', quiet=True)
    synonyms1 = set()
    synonyms2 = set()

    # Retrieve synonyms for words in string1
    for word in string1:
        synsets = wordnet.synsets(word)
        for synset in synsets:
            synonyms1.update(synset.lemma_names())

    # Retrieve synonyms for words in string2
    for word in string2:
        synsets = wordnet.synsets(word)
        for synset in synsets:
            synonyms2.update(synset.lemma_names())

    # Check if there is any intersection between the sets of synonyms
    return bool(synonyms1 & synonyms2)

# # Test the function
# string1 = '5 oranges'
# string2 = 'manadrins'
# result = are_synonymous(string1, string2)
# print(result)
