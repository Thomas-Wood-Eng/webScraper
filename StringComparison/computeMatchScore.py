######## string matching strat ########

'''
- Remove characters from both string
- Remove common words from both string
- Call lemmatization to 'normalize' words

The above will return a parsed string that can be used for comparison given to strings  (2 grocery items). To compare:
1. get a score from token comparison
2. get a score using using fuzzy matching (lavenstein)
* repeat above to compare all products with each other and output a list of groups

'''