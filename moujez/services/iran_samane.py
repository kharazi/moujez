from service import Service


class IranSamane(Service):
    def __init__(self, page):
        self.page = page
        # Service.__init__(self, page)

    # TODO: Using decorator for this part of code!
    def fetch_title(self):
        # return self.page.title.string
        return self.page.find('h1', {'class': 'title'}).text.strip()

    def fetch_subtitle(self):
        return self.page.find('div', {'class': 'subtitle'}).text.strip()

    def fetch_content(self):
        return self.page.find('div', {'class': 'body'}).text.strip()

    def fetch_news_code(self):
        return self.page.find('div', {'class': 'news_nav news_id_c'})
        
    def fetch_publication_date(self):
        return self.page.find('div', {'class': 'news_nav news_pdate_c'})

    def fetch_tags(self):
        return self.page.find('div', {'class': 'tags_title'})

    def fetch_category(self):
        return self.page.find('div', {'class': 'news_path'})



