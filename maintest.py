#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect(host="localhost", 
                     user="root",
                      passwd="", 
                      db="RT")
cur = db.cursor() 
cur.execute("SELECT * FROM tracks")

#db.close()

print "Content-type: text/html"

contents1='''

<html>
<body>
	<center>
	<form id='trackList'>
    <select size=3>
    '''    
print contents1

for row in cur.fetchall() :
	
	contents2='''
    <option onclick=audioHandler()>
    '''
	print contents2

	print row[0], row[1], row[2], row[3], row[4], row[5]

contents3='''
			<br>
    </select>
    </form>
    </center>

'''
print contents3


javascript_play_1='''
<script type="text/javascript">
var audio = new Audio;
function audioHandler() {
'''
db = MySQLdb.connect(host="localhost",
                     user="root",
                      passwd="",
                      db="RT")
cur = db.cursor() 
cur.execute("SELECT * FROM tracks where Id=%d")%(1)

javascript_play_2='''
	audio.setAttribute("src", '<?php echo "./audio/" . $output1[FileName]; ?>');
	audio.load();
	audio.play();
'''

print javascript1

javascript2='''
}</script>
'''
print javascript2

buttons='''
<center>
<br>
<input type="button" onclick="pauseAudio()" value="Pause">
<input type="button" onclick="playAudio()" value="Play">
<input type="button" onclick="nextAudio()" value="Next">
</center>
'''
print buttons


html_end='''
</body>
</html>
'''
print html_end
