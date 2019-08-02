import nltk
import re
import sys
sys.path.insert(1, 'Clustering')
import GetClusterData

"""
    <Created Date> Nov 9, 2018 </CreatedDate>    
    <About>
        A generic tokenizer implemented using nltk. The tokenizer REMOVES NUMBER ONLY terms       
    </About>
"""


tokens = list()    #list of tokes from the provided text (contains only alphabet tokens (numbers avoided) and also contains stop words)
filtered_list = list() #Filtered list containing tokens that are NOT stop words

#from the given text extract tokens
def tokenize_only(text):
    #first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    #filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

#get total count of tokens (NOT USED BUT USEFUL)
def countTotalTokens():
    dataRecords = []
    dataRecords = GetClusterData.GetDataFromDB()
    total_tokens = []
    for records in dataRecords:
        filtered_tokens = tokenize_only(records)
        for token in filtered_tokens:
            if token not in total_tokens:
                total_tokens.append(token)
    return len(total_tokens)