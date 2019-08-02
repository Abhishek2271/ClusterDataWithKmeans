import configparser

"""
    <Created Date> Nov 2, 2018 </CreatedDate>
    <LastUpdated> Nov 3, 2018 </LastUpdated>
    <About>
        Reads the ini file and extracts the specified section. The class does not do any further than parsing the file. 
        Reading secions and assigning values should be done separately
    </About>
"""

class ParserIni: 

    def Parse(self, Section):
        #Dictionary with KEY as the property inside sectino and VALUE is the correnponding value of the property. Port: 1433
        ResDictionary = dict()
        """r = set()
        r.add("a")
        r[0]"""        
        config = configparser.ConfigParser()
        #location of ini is inside this application folder. Tried using different location but did not work. So for now, use this location
        config.read("UserSettings.ini")
        print config.sections()
        options = config.options(Section)
        for option in options:
            ResDictionary[option] = config.get(Section, option)
        return ResDictionary
        """print options
        Host = config.get(Section, "host")
        print Host
        port = config.get(Section, "port")
        print port
        DBName = config.get(Section, "controldb")
        print DBName
        username = config.get(Section, "username")
        print username
        password = config.get(Section, "password")
        print password"""

    
    """ 
    Result = ReadIni('DBSettings')
    Host = Result["host"]
    print Host
    port = Result["port"]
    print port
    DBName = Result["controldb"]
    print DBName
    username = Result["username"]
    print username
    password = Result["password"]
    print password

    Result = ReadIni("Clustering_Settings")
    NumberofClusters = Result["number_of_clusters"]
    print NumberofClusters
    ignore_stop_words = str_to_bool(Result["ignore_stop_words"])
    print ignore_stop_words"""

