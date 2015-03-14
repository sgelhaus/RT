#!/usr/bin/python

import MySQLdb
print 

# Open database connection
db = MySQLdb.connect("localhost","root","3308","RT" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.

cursor.execute("SELECT * FROM tracks")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()

for row in data:
	print row[0], row[1]

# disconnect from server
db.close()
