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

def insert_user(username,password):
    conn=sqlite3.connect("user.db")
    c=conn.cursor()
    sql="insert into USER (username,password) values (?,?)"
    para=(username,password)
    c.execute(sql,para)
    conn.commit()
    conn.close()

def delete_user(username):
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    sql = "delete from USER where username='%s'"%username
    c.execute(sql)
    conn.commit()
    conn.close()

def check_user(username):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    cursor = c.execute("select * from user where username='%s'" % (username))
    temp=""
    for row in c:
        temp=row
    conn.close()
    return temp

def update_result(username,result):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    cursor = c.execute("update user set result='%s'  where username='%s'" % (result, username))
    conn.commit()
    conn.close()

def show():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    cursor=c.execute(''' select * from USER''')
    for row in c:
        print(row)
    conn.close()


if __name__=="__main__":
    # init_DB()
    # test_insert()
    # insert_user("MashiroCl123","123456")
    # delete_user("MashiroCl")
    # update_result("MashiroCl","I am the darkFlameMAster")
    # temp=check_user("saber123")
    # print(len(temp))
    # print(len(temp[0]))
    show()