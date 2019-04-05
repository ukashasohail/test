import sqlite3

conn = sqlite3.connect("file.db")

c = conn.scursor()

#create table command
c.execute("CREATE TABLE cis_te (first_name text,last_name text,  num int)")

#insert function
def insert_record(first_name,last_name,num):

    c.execute("INSERT INTO cis_te VALUES(?,?,?)",(first_name,last_name,num))
    conn.commit()

#show record function
def show_record(last_name1):

    c.execute("SELECT * FROM cis_te where last_name=(?)",(last_name1))
    print(c.fetchall())
#insert function call
insert_record()

#show record function call
show_record()


#update record query
# c.execute("UPDATE cis_te SET num=10000 where last_name='syed'")


conn.commit()
conn.close