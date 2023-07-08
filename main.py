from Advertiser import Advertiser
from Ad import Ad
from BaseAdvertising import BaseAdvertising

baseAdvertising = BaseAdvertising()
advertiser1 = Advertiser("name1")
advertiser2 = Advertiser("name2")
ad1 = Ad(advertiser1, "title1", "url1", "link1")
ad2 = Ad(advertiser2, "title2", "url2", "link2")
print(baseAdvertising.describeMe())
print(ad2.describeMe())
print(advertiser1.describeMe())
ad1.incViews()
ad1.incViews()
ad1.incViews()
ad1.incViews()
ad2.incViews()
ad1.incClicks()
ad1.incClicks()
ad2.incClicks()
print(advertiser2.getName())
advertiser2.setName("new name")
print(advertiser2.getName())
print(ad1.getClicks())
print(advertiser2.getClicks())
print(ad1.getViews())
print(Advertiser.getTotalClicks())
print(Advertiser.help())

