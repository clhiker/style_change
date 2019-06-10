import sqlite3
def init_DB():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE USER
           (username nchar NOT NULL,
           password  varchar NOT NULL,
           result   varchar );''')
    conn.commit()
    conn.close()

def test_insert():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('''insert into USER(username,password) 
                VALUES ('ADMIN','ADMIN')''')
    conn.commit()
    conn.close()

def show():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    cursor=c.execute(''' select * from USER''')
    for row in c:
        print(row)
    conn.close()

# init_DB()
test_insert()
show()