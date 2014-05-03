# -*- coding: utf-8 -*-
import re
from inspect import ismethod


class Service(object):

    def __init__(self, page):
        self.page = page
        # for i in dir(self):
        #     if i.startswith('fetch'):
        #         print 5 * "\n"
        #         print i
        #         getattr(self, i)()

    def fetch_title(self):

        def _is_a_title_candidate(tag):
            keywords = ["title", "Title", "TITLE"]

            if tag.has_attr('class'):
                for class_name in tag["class"]:
                    for keyword in keywords:
                        if keyword in class_name:
                            return True

            if tag.has_attr('id'):
                for keyword in keywords:
                    if keyword in tag["id"]:
                        return True

            if tag.name == "title":
                return True

            return False

        # print "-------------------\n" * 5
        #TODO: Need change
        for tag in self.page.find_all(_is_a_title_candidate):
            if tag.name == "title":
                return unicode(max(tag.text.strip().split("-"), key=len))

        # print "-------------------\n" * 5
        # print self.page.find("div", {"class": "PostTitle"})
        return u"عنوان خبر واکشی نشد!"

    def fetch_subtitle(self):
        pass

    def fetch_content(self):
        text = ''
    
        for i in self.page.find_all("p"):
          text += i.text.strip() + '\n'         
    
        if text.strip() == '':
            text = u"متنِ مقاله‌، مناسب خلاصه‌سازی نیست!"

        return unicode(text)

    def fetch_news_code(self):
        pass

    def fetch_publication_date(self):
        pass

    def fetch_tags(self):
        pass

    def fetch_category(self):
        pass

    def fetch_image(self):
        for tag in self.page.find_all("img"):
            if tag.parent.name == 'p':
                return tag['src']
        

