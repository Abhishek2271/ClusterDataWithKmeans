import sys
sys.path.insert(1, 'Utils')
import DBAction
import pandas as pd
from pandas import DataFrame
import pandas.io.sql as psql
import pyodbc
sys.path.insert(1, 'Clustering')
import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer

"""
    <Created Date> Nov 9, 2018 </CreatedDate>    
    <About>
        Query database to get the data required for clustering (that is, for computing the feature vector)       
    </About>
"""

#Get data from the database and return only the list of "Descriptions" as they are used for computing the featue vector (NOT USED)
def GetDataFromDB(dbConnection):   
    dataRecords = []     
    SQLQuery = "SELECT Title, Link, Description FROM tbl_ex_RSSData WITH(NOLOCK)"
    DBAction_inst = DBAction.DBAction()
    #conn = DBAction_inst.initiateConnection("localhost", 1433, "sa", "sandman", "DSApp_PCD_py")
    cursor = dbConnection.cursor()
    cursor.execute(SQLQuery)
    records = cursor.fetchall()
    #for now only get the contents for clustering so we only need the contents in the data frame
    for record in records:
        dataRecords.append(record[2])
        
    """cnxn = pyodbc.connect('Driver={{SQL Server Native Client 10.0}};Server={0};Database={1};Port={2};UID={3};PWD={4};Trusted_Connection = no;'.format("localhost", "DSApp_PCD_py", 1433, "sa", "sandman")) 
    df = psql.read_sql(SQLQuery, cnxn)"""
        
        #print self.dataRecords[0][:10]
    return dataRecords        
        #print dataset.sample(5)
            
#Get data from the database and return the dataframe containing "TITLE", "LINK" and "DESCRIPTION"
def CreateDataFrame(dbConnection):
    dataRecords = []
    dataRecords = GetDataFromDB(dbConnection)
    #print dataRecords
    """onlyContents = []
    i=0
    #get only contents from the results and list them for vectorization
    while i<len(dataRecords):
        onlyContents.append(dataRecords[i][2])
        i = i +1   
    print onlyContents[:1]"""
    dataframe = pd.DataFrame(dataRecords)
    return dataframe
    #print dataframe.head()

def GetDataFromDB_DataFrame(dbConnection):
    SQLQuery = "SELECT Title, Link, Description FROM tbl_ex_RSSData WITH(NOLOCK)"
    conn = pyodbc.connect('Driver={{SQL Server Native Client 10.0}};'
                                'Server={0};'
                                'Database={1};'                                
                                'Port={2};'
                                'UID={3};'
                                'PWD={4};'
                                'Trusted_Connection = no;'.format("localhost", "DSApp_PCD_py", 1433, "sa", "sandman"))
    sqlcmd = pd.read_sql(SQLQuery, dbConnection)
    df = pd.DataFrame(sqlcmd, columns=['Title','Link','Description'])
    #df.to_csv("d:\\sql_res.csv", encoding='utf-8')
    return df


#CreateDataFrame()
#print countTotalTokens()
#GetDataFromDB()