from sklearn.cluster import KMeans
import GetTfIdf
import pandas as pd
import GetClusterData
import sys
sys.path.insert(1, 'Utils')
import DBAction
sys.path.insert(1, 'Clustering')
import GetClusterData

from sklearn.decomposition import PCA
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.metrics.pairwise import cosine_similarity

#for now use the default value of clusters as 2. This can me optimized for automated calcluation but for now use the default value
num_clusters = 2

def beginClustering(Numberofclusters, useStopWords, dbConnection):    
    #need the casting here because python does not have types so this was being detected as string
    num_clusters = int(Numberofclusters)
    #initialize the kmeans object, no need to specify the number of iter, the number of iter by default is 300
    km = KMeans(n_clusters=num_clusters)
    #Get the tfidf details
    tfidf_obj = GetTfIdf.GetTfIdfMatrix(dbConnection)
    #the tf-idf matirx
    tfidf_matrix = tfidf_obj[0]
    #the tf-idf dataframe
    tfidf_dataframe = tfidf_obj[1]
    #the tf-idf vectorizer object
    tfidf_vectorizer = tfidf_obj[2]
    #Get the list of titles which will be useful for display
    allTitles = tfidf_obj[3]

    #compute the k means clusters
    km.fit(tfidf_obj[0])

    #labels are default since we have no pre-labled dataset
    clusters = km.labels_.tolist()
    centroids = km.cluster_centers_
    #show cluster results
    ShowClusterResults(km, allTitles, clusters, tfidf_vectorizer)
    #visualize results
    visualizeClusters(tfidf_matrix, allTitles, clusters)

#Get the results of Clustering
def ShowClusterResults(KMeansObj, allTitles, clusters, tfidf_vectorizer):
    order_centroids = KMeansObj.cluster_centers_.argsort()[:, ::-1]
    terms = tfidf_vectorizer.get_feature_names()

    #show top 5 terms in each clusters
    for i in range(num_clusters):
        top_ten_words = [terms[ind] for ind in order_centroids[i, :5]]
        print("Cluster {}: {}".format(i, ' '.join(top_ten_words)))

    #show the clustering results
    #texts = GetClusterData.GetDataFromDB()
    dataframe = pd.DataFrame(allTitles, index = clusters, columns = ["Text"])
    print dataframe
    """dataframe["text"] = texts
    dataframe["Cluster"] = clusters"""
    dataframe.to_csv("d:\\ClusteredData.csv", encoding='utf-8')

#visualize the cluster
def visualizeClusters(tfidf_matrix, allTitles, clusters):
    #the similarity distance here is required to convert the high dimensional feature vector matrix to 2 dimensional for plotting the graph
    dist = 1 - cosine_similarity(tfidf_matrix)
    abbv_title = []
    for Titles in allTitles:
        abbv_title.append(Titles[:10])

    #convert to 2D
    mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
    pos = mds.fit_transform(dist)  # shape (n_components, n_samples)
    #Start plotting
    xs, ys = pos[:, 0], pos[:, 1]
    cluster_colors = {0: '#1b9e77', 1: '#d95f02'}
    #create data frame that has the result of the MDS plus the cluster numbers and titles
    df = pd.DataFrame(dict(x=xs, y=ys, label=clusters, title = abbv_title)) 
    #group by cluster
    groups = df.groupby('label')
    # set up plot
    fig, ax = plt.subplots(figsize=(17, 9)) # set size
    ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
    #iterate through groups to layer the plot
    #note that I use the cluster_name and cluster_color dicts with the 'name' lookup to return the appropriate color/label
    for name, group in groups:
        ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, 
                color=cluster_colors[name], 
                mec='none')
        ax.set_aspect('auto')
        ax.tick_params(\
            axis= 'x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom='off',      # ticks along the bottom edge are off
            top='off',         # ticks along the top edge are off
            labelbottom='off')
        ax.tick_params(\
            axis= 'y',         # changes apply to the y-axis
            which='both',      # both major and minor ticks are affected
            left='off',      # ticks along the bottom edge are off
            top='off',         # ticks along the top edge are off
            labelleft='off')        
    ax.legend(numpoints=1)  #show legend with only 1 point
    #add label in x,y position with the label as the film title
    for i in range(len(df)):
        ax.text(df.ix[i]['x'], df.ix[i]['y'], df.ix[i]['title'], size=8)  
    plt.show() #show the plot

#DBAction_inst = DBAction.DBAction()
#conn = DBAction_inst.initiateConnection("localhost", 1433, "sa", "sandman", "DSApp_PCD_py")
#beginClustering(2, True, conn)