from service import Service


class NewsStudio(Service):
    def __init__(self, page):
        self.page = page

    def fetch_title(self):
        return self.page.find('div', {'id': 'docDiv3TitrMain'})

    def fetch_subtitle(self):
        return self.page.find('div', {'id': 'docDiv4LeadTitle'})

    def fetch_content(self):
        pass

    def fetch_news_code(self):
        return self.page.find('div', {'id': 'docDiv5InfoCode'})

    def fetch_publication_date(self):
        return self.page.find('div', {'id': 'docDiv3Date'})        

    def fetch_tags(self):
        # return self.page.find('div', {'id': 'docDiv3Date'})        
        pass

    def fetch_category(self):
        return self.page.find('div', {'id': 'docDiv1Menu1'})        
 
