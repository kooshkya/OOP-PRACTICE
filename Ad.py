class Advertiser:
    _nextId = 1

    @classmethod
    def generateNewId(cls):
        thisId = _nextId
        _nextId += 1
        return thisId

    def __init__(self, advertiser, title="Ad", imageUrl="", link=""):
        self._title = title
        self._imageUrl = imageUrl
        self._link = link
        self._advertiser = advertiser
        self._id = Advertiser.generateNewId()
        self._views = 0
        self._clicks = 0

    
    def getTitle(self):
        return self._title
    
    def setTitle(self, title):
        self._title = title

    def getImageUrl(self):
        return self._imageUrl

    def setImageUrl(self, imageUrl):
        self._imageUrl = imageUrl

    def getLink(self):
        return self._link

    def setLink(self, link):
        self._link = link

    def setAdvertiser(self, advertiser):
        self._advertiser = advertiser
    
    def getClicks(self):
        return self._clicks
    
    def getViews(self):
        return self._views
    
    def incClicks(self):
        self._clicks += 1
        self._advertiser.incClickes()

    def incViews(self):
        self._views += 1
        self._advertiser.incViews()

    @staticmethod
    def describeMe():
        return "I am the Ad class. I hold data like click count and view count for each of our ads."

print(Advertiser.help())