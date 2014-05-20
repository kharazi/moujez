'''
Create database script
'''
import sqlite3
conn = sqlite3.connect("log.db")

cursor = conn.cursor()
# cursor.execute("""
#     CREATE TABLE log 
#     (
#         submitted_time datatime,
#         title text,
#         source text,
#         summarized_text text
#     )
#     """)
c = 0
for i in cursor.execute("""
    SELECT * FROM log
    """):
    print i
    c += 1
    print "\n" * 3
print c
conn.commit()
conn.close()




