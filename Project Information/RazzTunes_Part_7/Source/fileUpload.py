#!/usr/bin/python
import MySQLdb 
import cgi, os 
import cgitb; cgitb.enable() 
## \file fileUpload.py Player handles track upload function within this python file
## \brief Project RazzTunes
## \details A web based music player
## \authors Team RazzTunes: Stephen Gelhaus, Parvinder Singh, Dan Sjaastad, Frank Erdesz
## \version beta

## A global variable for storing filename
fn = 0

## A global variable for opening files
open = 0

## A global variable for database information
db = 0

## A global variable cursor
cur = 0

## A global variable for form data
form = 0

## A global variable to output HTML coded messages
message = 0

try: # Windows needs this 
    import msvcrt 
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0 
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1 
except ImportError: 
    pass 


form = cgi.FieldStorage() 

fileitem = 0
fileitem = form['file'] 


database = MySQLdb.connect(host="localhost", 
						 user="root", 
						  passwd="", 
						  db="RT") 
						  
## @param db Brings the database variables into the main function
def main(db)
	if fileitem.filename: 
		fn = os.path.basename(fileitem.filename) 
		open('./audio/' + fn, 'wb').write(fileitem.file.read()) 
	
		cur = db.cursor() ;
		cur.execute("INSERT INTO tracks (Title, Artist, Album, Genre, FileName) VALUES ('Song Title1','Song Artist1','Song Album1','Song Genre1','" + fn + "');") ;
		db.close() ;
	
		message = 'The file was uploaded successfully.' 
 
  
	else: 
	   message = 'No file was uploaded' 
  
	print """\
	Content-Type: text/html\n
	<html><head>
	<style type="text/css">
	 html{ 
	  background: url(../images/bg.jpg) no-repeat center center fixed;  //Photo License: Creative Commons, www.flickr.com/photos/hexidecimal/6673189339
	  -moz-background-size: cover;
	  -webkit-background-size: cover;
	  background-size: cover;
	}
	</style>
	</head>
	<body>
	<p><center><b>%s</b></p>
	<p>
	<a href="/cgi-bin/maintest.py">Return</a></center>
	</body></html>
	""" % (message,) 


main(database)
