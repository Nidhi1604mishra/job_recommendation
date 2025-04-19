import spacy
import string

# load english nlp model from spacy
nlp = spacy.load("en_core_web_sm")

#Function to clean text
def clean_text(text):
    doc = nlp(text)             # Process the text
    
    tokens = []
    for token in doc:
        #Remove punctuation, stop-words, and non-alphabetic tokens
        if token.text.lower() not in nlp.Defaults.stop_words \
            and token.text not in string.punctuation \
                and token.is_alpha:
                    tokens.append(token.lemma_.lower())

    return " ".join(tokens) 
   