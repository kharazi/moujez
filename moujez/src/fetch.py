import urllib2
from inspect import ismethod
from bs4 import BeautifulSoup as Parser


class Fetch(object):    
    def __init__(self, url):
        self.url = url
        self.page = Parser(self._fetch())
        self.service = self._get_service()

    def _fetch(self):
        try:
            return urllib2.urlopen(self.url)
        except:
            raise urllib2.URLError, "There's a problem in internet connection"

    def _get_service(self):
        if self.page.find('a', {'href': 'http://iransamaneh.com'}):
            return 'iransamane'
        elif self.page.find('a', {'href': 'http://www.news-studio.com'}):
            return 'news-studio'
        else:
            return 'unknown'

