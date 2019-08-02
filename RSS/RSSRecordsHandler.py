import feedparser
import RSSFields
import ComputeHash
import DateTime

"""
    <Created Date> Nov 2, 2018 </CreatedDate>
    <About>
      This class:
        1. Get RSS data from the given URL
        2. Insert the RSS data to the database
    </About>
"""

_RssChannelFeilds = list()
_RssItemFields = list()
class ParseRss:

    URL = None
    SourceID = None
    Conn = None

    def __init__(self, _URL, _SourceID, _Conn):
        self.URL = _URL
        self.SourceID = _SourceID
        self.Conn = _Conn


    #Insert given RSS data to sql
    def InsertDatatoDB(self, RSSChannelElements):
        #DateTime.DateTime(RSSChannelElements.PublishedDate)
        #This conversion should work but currently gives wrong dates in some cases where date and the time (milli seconds) are somehow switched
        #instead of this the rss parser also provided already parsed dates, created date and time from that.
        #Pub_date = DateTime.DateTime.strftime(DateTime.DateTime(RSSChannelElements.PublishedDate), '%Y-%M-%d %H:%M:%S')        
        #Up_date = DateTime.DateTime.strftime(DateTime.DateTime(RSSChannelElements.UpdatedDate), '%Y-%M-%d %H:%M:%S')    
        sqlQuery = "INSERT INTO tbl_ex_RSSDATA (SourceID, Title, Link, Description, PublishedDate, UpdatedDate, ParsedDate, Hash)  Values (?, ?, ?, ?, ?, ?, getdate(), ?)"
        values = [self.SourceID, RSSChannelElements.Title, RSSChannelElements.Link, RSSChannelElements.Description, RSSChannelElements.PublishedDate, RSSChannelElements.UpdatedDate, RSSChannelElements.ComputedHash]
        #conn = DBAction.DBAction().initiateConnection("localhost", 1433, "sa", "sandman", "DSApp_PCD_py")
        Cursor = self.Conn.cursor()
        Cursor.execute(sqlQuery, values)
        self.Conn.commit()

    #From the given URL get the RSS data
    def GetData(self):
        self.NewsFeed = feedparser.parse(self.URL)
        #less details about channel from the parser so need to skip this. Channel details would be nice but RSS mostly does not have them
        """ChannelFields = RSSFields.RSSChannelElements()            
        for Feed in self.NewsFeed.feed:
            ChannelFields.Author  = None    #Most fields dont give this so for now, let this be non for safety.
            ChannelFields.managingEditor = None
            ChannelFields.webMaster = None
            ChannelFields.PublishedDate = None
            #ChannelFields.LastBuildDate = Feed.updated
            ChannelFields.Generator  = None
            ChannelFields.Description = None
            ChannelFields.Language = Feed.language
            print (len(self.NewsFeed.entries))
            _RssChannelFeilds.append(ChannelFields)"""
        #self.ChannedDetails = self.NewsFeed.
        for Entry in self.NewsFeed.entries:
            ChannelFields = RSSFields.RSSChannelElements()
            ChannelFields.Title = Entry.title
            ChannelFields.Description = Entry.summary
            ChannelFields.Link = Entry.link
            #somehow the python date parser is giving wrong dates so get the parsed dates instead anc construct the date manually
            ChannelFields.PublishedDate = str(Entry.published_parsed.tm_year) + "-" + str(Entry.published_parsed.tm_mon) + "-" + str(Entry.published_parsed.tm_mday) + " " + str(Entry.published_parsed.tm_hour) + ":"+ str(Entry.published_parsed.tm_min)  + ":" +  str(Entry.published_parsed.tm_sec) + "." + str(Entry.published_parsed.tm_yday)
            ChannelFields.UpdatedDate = str(Entry.published_parsed.tm_year) + "-" + str(Entry.published_parsed.tm_mon) + "-" + str(Entry.published_parsed.tm_mday) + " " + str(Entry.published_parsed.tm_hour) + ":"+ str(Entry.published_parsed.tm_min)  + ":" +  str(Entry.published_parsed.tm_sec) + "." + str(Entry.published_parsed.tm_yday)
            ChannelFields.ComputedHash = ComputeHash.ComputeHash(Entry.link)
            #_RssItemFields.append(ChannelFields)
            self.InsertDatatoDB(ChannelFields)


#p = ParseRss()
#p.GetData("http://feeds.bbci.co.uk/news/world/rss.xml")
"""entry = p.NewsFeed.entries[0]
print 'Post Title :',entry.title"""