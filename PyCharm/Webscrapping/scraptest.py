from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError, e:
        print e
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")
        elm = bsObj.find_all('a', href=True)
    except AttributeError, e:
        return None
    return elm

li = getTitle("https://www.indeed.com/jobs?q=azure&l=Dallas,+TX&start=20")
if li == None:
    print "Title could not be found"
else:
    for i in li:
        print i

a = {"h1"}

print type(a)