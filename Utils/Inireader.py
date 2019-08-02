import Iniparser
"""
    <Created Date> Nov 2, 2018 </CreatedDate>
    <LastUpdated>  Nov 3, 2018 </LastUpdated>
    <About>
        Reads the sections from the ini file and assignes values to all properties that should be read from the ini file
    </About>
"""
class Read:
        #these variables should ideally be static but since Python does not have static vars, so need to bind these to specific class instance
        def __init__(self):
        #read db settings
                self.Host = "Localhost"    
                self.DBName = "DSApp_PCD_py" 
                self.UserName = "sa"      
                self.Password = "sandman"
                self.Port = 14
                #read cluster related settings
                self.NumberofClusters = 1
                self.IgnoreStopWords = True

        #convert string to bool 
        def str_to_bool(self, s):
                if s == 'True':
                        return True
                elif s == 'False':
                        return False
                else:
                        raise ValueError
        
        #read individual properties from all sections and override default values
        def ReadIni(self):
                ini_parser = Iniparser.ParserIni()
                Result = ini_parser.Parse("DBSettings")
                #Result = iniparser.ReadIni('DBSettings')
                self.Host = Result["host"]
                print self.Host
                self.Port = Result["port"]
                print self.Port
                self.DBName = Result["controldb"]
                print self.DBName
                self.username = Result["username"]
                print self.username
                self.password = Result["password"]
                print self.password

                Result = ini_parser.Parse("Clustering_Settings")
                self.NumberofClusters = Result["number_of_clusters"]
                print self.NumberofClusters
                self.IgnoreStopWords = self.str_to_bool(Result["ignore_stop_words"])
                print self.IgnoreStopWords
        