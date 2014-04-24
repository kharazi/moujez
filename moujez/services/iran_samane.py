from service import Service


class IranSamane(Service):
    def __init__(self, page):
        self.page = page
        # Service.__init__(self, page)
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



