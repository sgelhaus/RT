#!/usr/bin/python

import MySQLdb
import os

db = MySQLdb.connect(host="localhost", 
                     user="root",
                      passwd="", 
                      db="RT")
cur = db.cursor() 
cur.execute("SELECT * FROM tracks")


print'''
<html>
<body>
	<center>
    <select size=3 id="selectBox" onchange="audioChooser();">
    '''    
    
for row in cur.fetchall() :
	
	print"""<option value='""",row[5],"""'>"""
	

	print row[0],row[1],row[2],row[3],row[4],row[5]

print'''
	<br>
    </select>
    </center>

'''


print'''
<script type="text/javascript">
var audio = new Audio;


function audioChooser() {
'''


print'''
var selectBox = document.getElementById("selectBox");
var selectedValue = selectBox.options[selectBox.selectedIndex].value;
var selectedValueSliced = selectedValue.slice(1);


var path = "../audio/"+selectedValueSliced;

audio.setAttribute("src", path);
audio.load();
audio.play();
}

function playAudio(){
if(!audio.paused){
    audio.pause();
    }
else{
    audio.play();
    }
	}

function pauseAudio(){
    audio.pause();
	}

function nextAudio(){
	}

function loopAudio(){
	if(audio.loop){
	audio.loop=false;
	}
	else{
	audio.loop=true;
	}
}

</script>
'''






print'''
<br>
<center>
<input type="image" src="../images/play.jpg" onclick="playAudio()" value="Play">
<input type="image" src="../images/pause.png"onclick="pauseAudio()" width="80" height="80" value="Pause">
<input type="button" onclick="nextAudio()" value="Next">

<br>
<input type="checkbox" onclick="loopAudio()" value="Loop"> Loop track
</center>
'''

print'''
<form enctype="multipart/form-data" action="upload.py" method="post">
<p>File: <input type="file" name="file"></p>
<p><input type="submit" value="Upload"></p>
</form>
'''




print'''
</body>
</html>
'''

#os.system('zenity --info --text=count')


db.close()
