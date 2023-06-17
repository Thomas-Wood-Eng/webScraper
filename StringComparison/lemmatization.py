import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


# feed in stop word removed string only for optimal lemmatization
# function returns list of lemmatized words of the string
def lemmatize_string(tockenizedText:list[str]):
    nltk.download('wordnet')
    wordnet_lematizer = WordNetLemmatizer()
    
    lemmatizedList = [wordnet_lematizer.lemmatize(token) for token in tockenizedText]

    return lemmatizedList


