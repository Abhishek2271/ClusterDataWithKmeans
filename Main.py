import sys
sys.path.insert(1, 'Utils')
import Iniparser
import DBAction
import Inireader
sys.path.insert(1, 'RSS')
import RSSRecordsHandler
sys.path.insert(1, 'Clustering')
import ClusterCore
"""
    <Created Date> Nov 9, 2018 </CreatedDate>
    <LastUpdated>  Dec 12, 2018 </LastUpdated>
    <About>
        This class:
            1. Reads from the ini file to get required values
            2. Calls RSS parsers to populate values
            3. Calls appropriate functions to Cluster, display results and visualize the clustered data items            
    </About>
"""

#read the ini file
class main:
    #Begin to parse and read the datasets
    def PopulateData(iniReader, dbConnection):        
        SQLQuery = "SELECT Sourceid, Type, SourceName, URL FROM [tbl_pj_SourceInfo] t1 WITH(NOLOCK), tbl_pj_SourceTypes t2 WITH(NOLOCK) WHERE t1.TypeID = t2.TypeID"
        cursor = dbConnection.cursor()
        cursor.execute(SQLQuery)
        records = cursor.fetchall()
        for row in records:
            if(row[1] == "RSS"):
                RSShandler = RSSRecordsHandler.ParseRss(row[3], row[0], dbConnection)
                RSShandler.GetData()
                print "RSS Data collected successfully from Source: {0}".format(row[2]) 

    
    #Read ini file to get the db related settings.
    ini_reader = Inireader.Read()
    ini_reader.ReadIni()
    #Get Database Connection
    DBAction_inst = DBAction.DBAction()
    conn = DBAction_inst.initiateConnection(ini_reader.Host, ini_reader.Port, ini_reader.UserName, ini_reader.Password, ini_reader.DBName)
    #Begin to populate the data in the SQL
    PopulateData(ini_reader, conn)
    #Begin clustering of the populated data
    ClusterCore.beginClustering(ini_reader.NumberofClusters, ini_reader.IgnoreStopWords, conn)