'''
Create database script
'''
import sqlite3
conn = sqlite3.connect("log.db")

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE log 
    (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT ,
        submitted_time datatime,
        title text,
        source text,
        summarized_text text,
        source_len real,
        summarized_text_len real,
        darsad real
    )
    """)

cursor.execute("""
    CREATE TABLE questions_table 
    (
        news_id int,
        question_1 text,
        question_2 text
    )

    """)

cursor.execute("""
    CREATE TABLE question_game_result
    (
        log_id int,
        name text,
        a11 text,
        a12 text,
        a21 text,
        a22 text,
        a31 text,
        a32 text
    )

    """)
c = 0
# for i in cursor.execute("""
#     SELECT * FROM log
#     """):
#     print i
#     c += 1
#     print "\n" * 3
# print c
conn.commit()
conn.close()




