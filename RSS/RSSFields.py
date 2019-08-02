"""
    <Created Date> Dec 5, 2018 </CreatedDate>
    <About>
      Class containing RSS Fields currently being extracted from the RSS links
        The channel elements are specific to channel, 
        RSS fields are specific to individual "items"
    </About>
"""
class RSSFieldElements:
    Title = None
    Link = None
    Description = None
    PublishedDate = None
    UpdatedDate = None
    ComputedHash = None

    #Unused Fields.
    Author = None
    Category = None
    Comments = None
    Contributers = None
    Source = None
    Enclosure = None


class RSSChannelElements:
    Language  = None    #Same for all contents of one rss link.
    managingEditor = None
    webMaster = None
    PublishedDate = None
    LastBuildDate = None
    Generator  = None
    Description = None
    Author = None
