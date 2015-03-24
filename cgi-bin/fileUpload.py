#!/usr/bin/python
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
	message = 'The file was uploaded successfully'
   
else:
   message = 'No file was uploaded'
   
print """\
Content-Type: text/html\n
<html><body>
<p>%s</p>
</body></html>
""" % (message,)
