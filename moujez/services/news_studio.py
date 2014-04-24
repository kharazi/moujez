from service import Service


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
 
