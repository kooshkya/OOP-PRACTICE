class Advertiser:
    _nextId = 1
    _instances = []

    @classmethod
    def generateNewId(cls):
        thisId = _nextId
        _nextId += 1
        return thisId
    
    @classmethod
    def getTotalClicks(cls):
        result = 0
        for i in cls._instances:
            result += i.getClicks()
        return result


    def __init__(self, name="advertiser"):
        self._name = name
        self._id = Advertiser.generateNewId()
        self._views = 0
        self._clicks = 0
        Advertiser._instances.append(self)

    
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name

    @staticmethod
    def help():
        helpText = "Class Advertiser has the below fields:\n"
        helpText += "id: This is a unique token give to each instance of Advertiser.\n"
        helpText += "name: This is a textual name assigned to each advertiser.\n"
        helpText += "views: This is the number of times that this advertiser's ad has been viewed\n"
        helpText += "clicks: This is the number of times that the advertiser's ad has been clicked on\n"
        return helpText
    
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
        return "I am the Advertiser class. I hold data like click count and view count for each of our clients."

print(Advertiser.help())