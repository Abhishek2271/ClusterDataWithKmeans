# import statements
import nltk
import re
import sys
sys.path.insert(1, 'Clustering')
import Tokenizer
import pandas as pd

"""
    <Created Date> Nov 9, 2018 </CreatedDate>    
    <About>
        Use NLTK to get a stop words filter for tokens. The stop word list is a default one provided by nltk with nothing added       
    </About>
"""


stopwords = nltk.corpus.stopwords.words('english')  #Get standard stop words as defined in nltk corpus
print stopwords[:10]

tokens = list()    #list of tokes from the provided text (contains only alphabet tokens (numbers avoided) and also contains stop words)
filtered_list = list() #Filtered list containing tokens that are NOT stop words

#From the list of "tokens" remove the stop words. Input here is tokens so we need a simple tokenizer to get the tokens
def remove_stopwords(tokens):
    for token in tokens:
        if token not in stopwords:
            filtered_list.append(token)
    return filtered_list

"""
#Test out if the filtering is working
tokens =  Tokenizer.tokenize_only("this is a teXt 1")
print tokens
print remove_stopwords(tokens)
#sample data frames
data = {"col1" : [1,2] ,"col2": [2,3] , "col3":[3,4]}
data2 = [[1,2], [1,3]]
data3 = [1,2,3,4] 
#Create a data frame with the tokens
dataFrame = pd.DataFrame(data3,columns = ["data"])

print dataFrame
"""
Data = [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46,
         79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]
  
#df = pd.DataFrame(Data)
#print df
"""from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt
# create blobs
data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.6, random_state=50)
# create np array for data points
points = data[0]
# create scatter plot
plt.scatter(data[0][:,0], data[0][:,1], c=data[1], cmap='viridis')
plt.xlim(-15,15)
plt.ylim(-15,15)
plt.show()

from sklearn.feature_extraction.text import TfidfVectorizer 
import operator
 
corpus=["this car got the excellence award",\
         "good car gives good mileage",\
         "this car is very expensive",\
         "the company is growing with very high production",\
         "this company is financially good"]
 
vocabulary = set()
for doc in corpus:
    vocabulary.update(doc.split())
 
vocabulary = list(vocabulary)
word_index = {w: idx for idx, w in enumerate(vocabulary)}
 
tfidf = TfidfVectorizer(vocabulary=vocabulary)
 
# Fit the TfIdf model
tfidf.fit(corpus)
tfidf.transform(corpus)
 
for doc in corpus:
    score={}
    print(doc)
    # Transform a document into TfIdf coordinates
    X = tfidf.transform([doc])
    for word in doc.split():
        score[word] = X[0, tfidf.vocabulary_[word]]
    sortedscore = sorted(score.items(), key=operator.itemgetter(1), reverse=True)
    print("/n", sortedscore)"""