import nltk
import re
import sys
sys.path.insert(1, 'Clustering')
import Tokenizer
from nltk.stem.snowball import SnowballStemmer

"""
    <Created Date> Nov 9, 2018 </CreatedDate>    
    <About>
        A generic snowball stemmer implemented using nltk. The tokenizer REMOVES NUMBER ONLY terms       
    </About>
"""

stemmer = SnowballStemmer("english")

tokens = list()
uniqueStems = list()

#From the list of "tokens" remove the stop words. Input here is tokens so we need a simple tokenizer to get the tokens
def tokenize_and_stem(tokens):
    stems = [stemmer.stem(t) for t in tokens]
    for stem in stems:
        if stem not in uniqueStems:
            uniqueStems.append(stem)
    return uniqueStems
    
"""
tokens = Tokenizer.tokenize_only("This is a testing test tested for rest ")
print tokenize_and_stem(tokens)"""
