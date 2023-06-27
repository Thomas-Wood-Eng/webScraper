import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_stopwords(text):
    # Download stopwords and punkt
    nltk.download('stopwords', quiet=True)
    nltk.download('punkt', quiet=True)

    # Get the list of stopwords
    stop_words = set(stopwords.words('english'))

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords
    filtered_tokens = [word for word in tokens if word.casefold() not in stop_words]

    # Reconstruct the string without stopwords
    # filtered_text = ' '.join(filtered_tokens)

    return filtered_tokens

