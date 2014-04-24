import urllib2
from inspect import ismethod
from bs4 import BeautifulSoup as Parser


class Service(object):
    def __init__(self, page):
        for i in dir(self):
            if i.startswith('fetch'):
                print 5 * "\n"
                print i
                getattr(self, i)()

class NewsStudio(Service):
    def __init__(self, page):
        self.page = page

    def fetch_title(self):
        print self.page.find('div', {'id': 'docDiv3TitrMain'})

    def fetch_subtitle(self):
        print self.page.find('div', {'id': 'docDiv4LeadTitle'})

    def fetch_content(self):
        pass

    def fetch_news_code(self):
        print self.page.find('div', {'id': 'docDiv5InfoCode'})

    def fetch_publication_date(self):
        print self.page.find('div', {'id': 'docDiv3Date'})        

    def fetch_tags(self):
        # print self.page.find('div', {'id': 'docDiv3Date'})        
        pass

    def fetch_category(self):
        print self.page.find('div', {'id': 'docDiv1Menu1'})        
 


class IranSamane(Service):
    def __init__(self, page):
        self.page = page
        # Service.__init__(self, page)
        self.fetch_title()
    def fetch_title(self):
        # return self.page.title.string
        print self.page.find('h1', {'class': 'title'})

    def fetch_subtitle(self):
        print self.page.find('div', {'class': 'subtitle'})

    def fetch_content(self):
        print self.page.find('div', {'class': 'body'})

    def fetch_news_code(self):
        print self.page.find('div', {'class': 'news_nav news_id_c'})
        
    def fetch_publication_date(self):
        print self.page.find('div', {'class': 'news_nav news_pdate_c'})

    def fetch_tags(self):
        print self.page.find('div', {'class': 'tags_title'})

    def fetch_category(self):
        print self.page.find('div', {'class': 'news_path'})





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


test = Fetch("http://www.fardanews.com/fa/news/334201/%D9%82%D9%88%D9%84%E2%80%8C%D8%AA%D9%88%D9%84%DB%8C%D8%AF%DA%86%D9%86%D8%AF%DB%8C%D9%86%E2%80%8C%D9%85%DB%8C%D9%84%DB%8C%D9%88%D9%86%DB%8C%E2%80%8C%D8%A8%D8%B4%DA%A9%D9%87%E2%80%8C%D9%86%D9%81%D8%AA%E2%80%8C%D8%A7%D8%B2%D8%B3%D9%88%DB%8C%E2%80%8C%D8%B2%D9%86%DA%AF%D9%86%D9%87")
IranSamane(test.page)