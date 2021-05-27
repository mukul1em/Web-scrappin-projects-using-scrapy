import sqlite3

conn = sqlite3.connect('quotes.db')
curr = conn.cursor()

# curr.execute("""create table quotes_table(
#     title text,
#     author text,
#     tag text
#     )""")


curr.execute("""insert into quotes_table values ('python is awesom','buildwithpython', 'python')""")

conn.commit()
conn.close()



