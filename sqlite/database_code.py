import sqlite3

conn = sqlite3.connect("file.db")

c = conn.cursor()

#create table command
# c.execute("CREATE TABLE employee (first_name text,last_name text,  num int)")

#insert function
def insert_record(first_name,last_name,emp_num):

    c.execute("INSERT INTO employee VALUES(?,?,?)",(first_name,last_name,emp_num))
    conn.commit()

#show record function
def show_record():

    c.execute("SELECT * FROM employee where first_name='hamza'")
    print(c.fetchone())
#insert function call
# insert_record('syed','osama',5000)
# insert_record('hamza','hameed',6000)
# insert_record('ammar','sleepyhead',1000)

#show record function call
show_record()


#update record query
# c.execute("UPDATE cis_te SET num=10000 where last_name='syed'")


conn.commit()
conn.close