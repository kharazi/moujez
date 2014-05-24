# -*- coding: utf-8 -*-
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
        try:
            result = self.page.find('div',
                                    {'class': 'tags_title'}
                                    ).text.strip().split(u'،')
            result[0] = result[0][result[0].find(':') + 1:]
            return [item.strip() for item in result]
        
        except Exception, e:
            print str(e)


    def fetch_category(self):
        return self.page.find('div', {'class': 'news_path'})

    def fetch_image(self):
        try:
            return self.page.find('div', {'class': 'body'}).find('img')['src']
        except:
            return None