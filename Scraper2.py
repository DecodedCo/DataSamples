from BeautifulSoup import BeautifulSoup #import bs4
import json #import the json library
import urllib2 #import url handling
url = urllib2.urlopen("http://graph.facebook.com/proctergamble")
content = url.read() #read the content returned
soup = BeautifulSoup(content) #import to soup
newDictionary=json.loads(str(soup)) #process as json
print newDictionary["likes"] #get the likes