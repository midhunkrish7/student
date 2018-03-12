import MySQLdb
 
db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="",     # password
                     db="STUDENT")   # name of the database
 
# Create a Cursor object to execute queries.
cur= db.cursor()
 
# Select data from table using SQL query.
cur.execute("SELECT * FROM tab2")
 
# print the first  second & third columns      
for col in cur.fetchall() :
    print col[0], "|", col[1]

