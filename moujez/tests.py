# -*- coding: utf-8 -*-
from __future__ import division
import sqlite3 
import datetime

import pickle
from src.summarize import Summarizer
from services.iran_samane import IranSamane
from services.news_studio import NewsStudio
from src.fetch import Fetch
from bs4 import BeautifulSoup as Parser


conn = sqlite3.connect("log.db")
cursor = conn.cursor()

# archive_asriran_file = open("archive_asriran.html", "r")
archive_tabnak_file = open("archive_tabnak.html", "r")

# aes = Parser(archive_asriran_file).find_all("a", {"class": "title4"})
aes = Parser(archive_tabnak_file).find_all("a", {"class": "title5"})
c = 0
for i in aes:
    c += 1
    print c
    try:
        summarizer = Summarizer()
        page = Fetch(i["href"])
        if page.service == 'iransamane':
            service = IranSamane(page.page)
        elif page.service == 'news-studio':
            service = NewsStudio(page.page)
        else:
            service = Service(page.page)

        content = service.fetch_content()
        summarized = summarizer.summarize(content)
        print "end summarize"
        res = {
            'summarized': summarized,
            'title': service.fetch_title(),
            'tags': service.fetch_tags(),
            'image': service.fetch_image(),
        }

        # For log
        sums = ""
        for i in summarized:
            sums += i
        koft =  len(sums) / len(content) * 100.0
        print koft
        log = (datetime.datetime.now(), res['title'], content, sums, len(content), len(sums), koft) 
        cursor.execute('INSERT INTO log (submitted_time, title, source, summarized_text, source_len, summarized_text_len, darsad) VALUES (?,?,?,?,?,?,?)', log)
        conn.commit()
    except:
        print "nashooood", c
    # 



# from src.fetch import Fetch


# test = Fetch("http://www.fardanews.com/fa/news/334201/%D9%82%D9%88%D9%84%E2%80%8C%D8%AA%D9%88%D9%84%DB%8C%D8%AF%DA%86%D9%86%D8%AF%DB%8C%D9%86%E2%80%8C%D9%85%DB%8C%D9%84%DB%8C%D9%88%D9%86%DB%8C%E2%80%8C%D8%A8%D8%B4%DA%A9%D9%87%E2%80%8C%D9%86%D9%81%D8%AA%E2%80%8C%D8%A7%D8%B2%D8%B3%D9%88%DB%8C%E2%80%8C%D8%B2%D9%86%DA%AF%D9%86%D9%87")
# farda = IranSamane(test.page)
# print farda.fetch_title()
# print type(farda.fetch_title())
# print





# a = SimpleSummarizer()

# print a.summarize(u'سلام خوبی. مرسی!',1)

# a = Summarizer()
# a.sentences_number = 60
# print a._find_num_sentences()
# print a.summarize(u'سلام خوبی. مرسی! I am a teacher!')


# summarizer = Summarizer()
# a = u"http://www.asriran.com/fa/news/332468/%D9%BE%DB%8C%D8%A7%D9%85-%D8%B3%DB%8C%D8%AF-%D9%85%D8%AD%D9%85%D8%AF-%D8%AE%D8%A7%D8%AA%D9%85%DB%8C-%D8%A8%D9%87-%DA%A9%D9%86%DA%AF%D8%B1%D9%87-%D9%8A%DA%A9-%D8%AD%D8%B2%D8%A8"
# link = u'http://alef.ir/vdcc10qix2bqi08.ala2.html?224430'

# page = Fetch(a)
# service = NewsStudio(page.page)

# print service.fetch_title()
# print service.fetch_content()
# page = Fetch(a)
# if page.service == 'iransamane':
#     service = IranSamane(page.page)
# elif page.service == 'news-studio':
#     service = NewsStudio(page.page)

# content = service.fetch_content()
# for i in  summarizer.summarize(content):
#     print i


# summarizer = Summarizer()

# # a = request.args.get('a', 0, type=str)
# a = "http://alef.ir/vdce7e8wnjh8wei.b9bj.html?224405"
# summarizer = Summarizer()
# # a = u"http://www.asriran.com/fa/news/332468/%D9%BE%DB%8C%D8%A7%D9%85-%D8%B3%DB%8C%D8%AF-%D9%85%D8%AD%D9%85%D8%AF-%D8%AE%D8%A7%D8%AA%D9%85%DB%8C-%D8%A8%D9%87-%DA%A9%D9%86%DA%AF%D8%B1%D9%87-%D9%8A%DA%A9-%D8%AD%D8%B2%D8%A8"
# page = Fetch(a)
# # print page.page
# if page.service == 'iransamane':
#     service = IranSamane(page.page)
# elif page.service == 'news-studio':
#     service = NewsStudio(page.page)

# print "fetching content"
# print type(service.fetch_title())
# # print type(service.fetch_content())
# content = service.fetch_content()
# # print "end fetching"
# # print content
# summarized = summarizer.summarize(content)
# print summarized
# # print "end summarize"