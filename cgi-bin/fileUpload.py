#!/usr/bin/python
import MySQLdb
import cgi, os
import cgitb; cgitb.enable()

try: # Windows needs this
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()

# holds the file
fileitem = form['file']

if fileitem.filename:
	fn = os.path.basename(fileitem.filename)
	open('./audio/' + fn, 'wb').write(fileitem.file.read())
	
	db = MySQLdb.connect(host="localhost", 
                     user="root",
                      passwd="", 
                      db="RT")
	cur = db.cursor() 
	cur.execute("INSERT INTO tracks (Title, Artist, Album, Genre, FileName) VALUES ('Song Title1','Song Artist1','Song Album1','Song Genre1','" + fn + "');")
	db.close()
	
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


