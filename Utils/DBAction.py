import pyodbc
"""
    <Created Date> Nov 2, 2018 </CreatedDate>
    <LastUpdated> Nov 3, 2018 </LastUpdated>
    <About>
        Class for now just  1. Returns a connection object
                            2. Can be used to execute sql queries
        Can be extended to create dataframes  
    </About>
"""
class DBAction:

    def initiateConnection(self, Host, Port, UserName, Password, DBName):
        try:
            conn = pyodbc.connect('Driver={{SQL Server Native Client 10.0}};'
                                'Server={0};'
                                'Database={1};'                                
                                'Port={2};'
                                'UID={3};'
                                'PWD={4};'
                                'Trusted_Connection = no;'.format(Host, DBName, Port, UserName, Password))
            #conn = pyodbc.connect('Driver={SQL Server Native Client 10.0};Server=localhost;Port = 1433;Database=DSApp_PCD_py;UID=sa;PWD=sandman;Trusted_Connection=no')
            """Cursor = conn.cursor()
            SqlCommand = "INSERT INTO NewTable VALUES (?)"
            Values = ["user"]
            Cursor.execute(SqlCommand, Values)
            conn.commit()"""
            return conn
        except Exception as exp:
            print "There was an error. Details: " + exp.message

    #Execute provided query
    def ExecuteQuery(self, conn, query):
        try:
            cursor = conn.cursor()
            SQLCommand = query
            cursor.execute(SQLCommand)
            conn.commit()
        except Exception as exp:
            print "There was an exception: " + exp.message



    #initiateConnection("localhost", 1433, "sa", "sandmans", "DSApp_PCD_py")
    

    


