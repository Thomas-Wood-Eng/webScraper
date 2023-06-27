######## string matching strat ########
from removeCharacters import remove_special_characters
from removeCommonWords import remove_stopwords
from lemmatization import lemmatize_string
from synnanomMapping import are_synonymous
from tokenComparison import token_compare

'''
- Remove characters from both string
- Remove common words from both string
- Call lemmatization to 'normalize' words

The above will return a parsed string that can be used for comparison given to strings  (2 grocery items). To compare:
1. get a score from token comparison
2. get a score using using fuzzy matching (lavenstein)
* repeat above to compare all products with each other and output a list of groups

'''
class ProductMatch:
    def clean(self, input:str):
        input = input.lower()
        cleaned_string = remove_special_characters(input)

        cleaned_string = remove_stopwords(cleaned_string)

        cleaned_string = lemmatize_string(cleaned_string)

        return cleaned_string

    # return a match score of how similar a sample string is to a reference string
    def compute_score(self, ref:str, sample:str):

        string1 = self.clean(ref)
        string2 = self.clean(sample)

        # returns 1 if two strings are deemed to be synnonmous
        synon_score = int(are_synonymous(string1, string2))

        tokenComparison_score = token_compare(string1, string2)

        match_score = ((1.7 * synon_score) + (0.7 * tokenComparison_score)) / 2


        print(f"SYNON SCORE: {synon_score}")
        print(f"TOKEN SCORE SCORE: {tokenComparison_score}")
        print(f"MATCH SCORE: {match_score}")

testObj = ProductMatch()

testObj.compute_score("Fairtrade Organic Banana", "Organic Bananas Bunch (8-10 count) (ripe in 3 days)")