#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="3308", # your password
                      db="RT") # name of the data base
cur = db.cursor() 
cur.execute("SELECT * FROM tracks")

# print all the first cell of all the rows
for row in cur.fetchall() :
    scrollist = row[0], row[1], row[2], row[3], row[4], row[5]
    
db.close()

print "Content-type: text/html"

contents='''

<html>
<head>
	<form id='trackList'>
    <select size=3>
    <option> print "Database version : %s " % data <br> </option>
    type <br>
    type <br>
    haha <br>
    </select>
    </form>
</head>
</html>


'''
print contents
