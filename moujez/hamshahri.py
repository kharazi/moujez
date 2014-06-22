# -*- coding: utf-8 -*-
import codecs
import sqlite3
import pickle

conn = sqlite3.connect("log.db")
cursor = conn.cursor()

# with codecs.open('summarized.xml', 'a', encoding='utf8') as f:
    
    # f.write("""<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<!DOCTYPE HAMSHAHRI SYSTEM "hamshahri.dtd">\n<HAMSHAHRI>""")

    # style = u"""<DOC>\n<DOCID>%d</DOCID>\n<DOCNO>H-750402-1S1</DOCNO>\n<DATE>1996-06-22</DATE>\n<CAT xml:lang="fa">ادب و هنر</CAT>\n<CAT xml:lang="en">Literature and Art</CAT>\n<TEXT>\n%s\n</TEXT>\n</DOC>\n"""
l = []
for i in cursor.execute("select * from log"):
    l.append(i[3])

print type(l)
pickle.dump(l, open("source.pk", "w"))
