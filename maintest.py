#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="", # your password
                      db="RT") # name of the data base
cur = db.cursor() 
cur.execute("SELECT * FROM tracks")

# print all the first cell of all the rows
#for row in cur.fetchall() :
#    data = row[0], row[1], row[2], row[3], row[4], row[5]
    
#db.close()

print "Content-type: text/html"

contents='''

<html>
<head>
	<form id='trackList'>
    <select size=3>
    '''    
print contents

for row in cur.fetchall() :
	
	contents2='''
    <option>
    '''
	print contents2

	print row[0], row[1], row[2], row[3], row[4], row[5]

contents3='''
			<br>
    </select>
    </form>
</head>
</html>
'''
print contents3
