import sqlite3
def init_DB():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE USER
           (NAME varchar(50) NOT NULL,
           PASSWORD  VARCHAR(50) NOT NULL,
           CONTENT_PIC);''')
    conn.commit()
    conn.close()