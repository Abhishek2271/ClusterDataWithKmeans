from sklearn.feature_extraction.text import TfidfVectorizer
import sys
sys.path.insert(1, 'Clustering')
import GetClusterData
import Tokenizer
import GetClusterData

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pandas as pd

"""
    <Created Date> Nov 9, 2018 </CreatedDate>
    <LastUpdated>  Dec 12, 2018 </LastUpdated>
    <About>
        represent the document in terms of feature vectors to get them clustered.
        The feature vector is a row matrix which each element representing the tf-idf of a term in the document. 
        It seems that we dont need to pass the tokens but only the contents and the vectorizer will tokenize the document as per the tokenizer we specified 
            and give tf.idf as a matrix          
    </About>
"""


#define vectorizer parameters
def GetTfIdfMatrix(dbConnection):
    #get the contents to create a tf-idf matrix
    #the contents contains the desctiption from the "Description" column in the tbl_ex_RSSDatabase db. 
    #contents = GetClusterData.GetDataFromDB()
    contents_dataframe = GetClusterData.GetDataFromDB_DataFrame(dbConnection)
    contents = contents_dataframe["Description"].tolist()
    #print contents
    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                    min_df=0, stop_words='english',
                                    use_idf=True, tokenizer=Tokenizer.tokenize_only, ngram_range=(1,3))   
    #get the tdf-idf matrix, the contents here should be the list of contents that we want to cluster,
    #in our case, it is the description of the news items.
    tfidf_matrix = tfidf_vectorizer.fit_transform(contents) #fit the vectorizer to synopses
    #print(tfidf_matrix.shape)
    #this prints the list of features used to get the tf-idf matrix
    #terms = tfidf_vectorizer.get_feature_names()
    #print tfidf_matrix.shape
    #print terms
    #print tfidf_matrix    
    #get the data frame as well, this can be used while plotting the clustered results    
    dataframe = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names())  
    #return both matrix -> Used for computing the cluster and DataFrame-> used for plotting the clustered results and also the list of Titles (only for displaying results)
    return [tfidf_matrix, dataframe, tfidf_vectorizer, contents_dataframe["Title"].tolist()]

#retur=[]
#retur = GetTfIdfMatrix()