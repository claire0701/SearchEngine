import urllib2
from BeautifulSoup import *
from urlparse import urljoin


# Create a list of words to ignore
ignoreWords = set(['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it'])


class Crawler:

    # Initialize the crawler with the name of database
    def __init__(self, dbname):
        pass
    
    def __del__(self):
        pass

    def dbcommit(self):
        pass
    
    # Auxilliary function for getting an entry if and adding
    # if if it's not present
    def getentryid(self, table, field, value, createnew=True):
        return None

    def addtoindex(self, url, soup):
        return 'Indexing %s' % url
    
    # Extract the text from an HTML page (no tags)
    def gettextonly(self, soup):
        return None

    # Separate the words by any non-whitespace character
    def separatewords(self, text):
        return None

    # Return true if this url is already indexed
    def isindexed(self, url):
        return False

    # Add a link between two pages
    def addlinkref(self, urlfrom, urlto, linktext):
        pass
    
    # Starting with a list of pages, do a breadth
    # first search to t he given depth, indexing pages as we go
    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    c = urllib2.urlopen(page)
                except:
                    print "Could not open %s" % page
                    continue
                soup = BeautifulSoup(c.read())
                self.addtoindex(page, soup)

                links = soup('a')
                for link in links:
                    if 'href' in dict(link.attrs):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1:
                            continue
                        url = url.split('#')[0]  # remove the location portion
                        if url[0:4] == 'http' and not self.isindexed(url):
                            newpages.add(url)
                        linktext = self.gettextonly(link)
                        self.addlinkref(page, url, linktext)
                self.dbcommit()
            pages = newpages

    # Create the database tables
    def createindextables(self):
        pass
