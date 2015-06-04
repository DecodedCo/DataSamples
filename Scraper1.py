from bs4 import BeautifulSoup
import requests
links = [] #store all links found
def visitUrl(URL):
	print "visiting: ", URL
	r  = requests.get(URL)
	return r.text

def linkHunter(TEXT):
	soup = BeautifulSoup(TEXT)
	for l in soup.find_all('a'):
	    links.append(l.get('href'))
	for link in links:
		print link
		if link and "http:" in link:
			visitUrl(link)

data = visitUrl("http://www.theguardian.com/international")
linkHunter(data)	



