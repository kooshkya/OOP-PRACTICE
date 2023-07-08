class BaseAdvertising:
    _nextId = 1

    @classmethod
    def generateNewId(cls):
        thisId = BaseAdvertising._nextId
        BaseAdvertising._nextId += 1
        return thisId
    
    def __init__(self):
        self.id = self.generateNewId()
        self._clicks = 0
        self._views = 0

    def getClicks(self):
        return self._clicks
    
    def getViews(self):
        return self._views

    def incClicks(self):
        self._clicks += 1

    def incViews(self):
        self._views += 1

    @staticmethod
    def describeMe():
        return "I am the base class for Ad and Advertiser entities."