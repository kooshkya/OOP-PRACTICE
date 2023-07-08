from BaseAdvertising import BaseAdvertising

class Advertiser(BaseAdvertising):
    _instances = []

    @classmethod
    def getTotalClicks(cls):
        result = 0
        for i in cls._instances:
            result += i.getClicks()
        return result


    def __init__(self, name="advertiser"):
        super().__init__()
        self._name = name
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
    
    @staticmethod
    def describeMe():
        return "I am the Advertiser class. I hold data like click count and view count for each of our clients."
