from BaseAdvertising import BaseAdvertising

class Ad(BaseAdvertising):
    def __init__(self, advertiser, title="Ad", imageUrl="", link=""):
        super().__init__()
        self._title = title
        self._imageUrl = imageUrl
        self._link = link
        self._advertiser = advertiser

    
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
    
    def incClicks(self):
        self._clicks += 1
        self._advertiser.incClicks()

    def incViews(self):
        self._views += 1
        self._advertiser.incViews()

    @staticmethod
    def describeMe():
        return "I am the Ad class. I hold data like click count and view count for each of our ads."
