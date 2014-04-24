from inspect import ismethod


class Service(object):
    def __init__(self, page):
        self.page = page
        for i in dir(self):
            if i.startswith('fetch'):
                print 5 * "\n"
                print i
                getattr(self, i)()

    def fetch_title(self):
        pass 

    def fetch_subtitle(self):
        pass

    def fetch_content(self):
        pass

    def fetch_news_code(self):
        pass

    def fetch_publication_date(self):
        pass

    def fetch_tags(self):
        pass

    def fetch_category(self):
        pass 