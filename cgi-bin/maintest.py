#!/usr/bin/python

import MySQLdb
import os
import cgi, os
import cgitb; cgitb.enable()

db = MySQLdb.connect(host="localhost", 
                     user="root",
                      passwd="", 
                      db="RT")
cur = db.cursor() 
cur.execute("SELECT * FROM tracks")


print'''
<html>
<head>
<title>Project RazzTunes</title>
</head>
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
    audio.play();
	}

function pauseAudio(){
    audio.pause();
	}
function stopAudio(){
	audio.pause();
	audio.load();
}

function nextAudio(){
	var selectedValue = selectBox.options[selectBox.selectedIndex].value;
	var selectedValueSliced = selectedValue.slice(1);
	var path = "../audio/"+selectedValueSliced;

	audio.setAttribute("src", path);
	audio.load();
	audio.play();
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
<input type="image" src="../images/play.png" onclick="playAudio()" value="Play">
<input type="image" src="../images/pause.png" onclick="pauseAudio()" value="Pause">
<input type="image" src="../images/stop.png" onclick="stopAudio()" value="Stop">

<input type="button" onclick="nextAudio()" value="Next">

<br>
<input type="checkbox" onclick="loopAudio()" value="Loop"> Loop track
</center>


<form enctype="multipart/form-data" action="fileUpload.py" method="post">
<input type="file" name="file">
<button type="submit" style="background:transparent; border:none; color:transparent;"><img src="../images/upload.png" /></button>
</form>
'''



print'''
</body>

<footer>

<p style="position: absolute; bottom: 0; width: 100%; text-align: center;">
<a href="https://github.com/stge0958/RT">
<img src="../images/info.png">
</a>
</p>

</footer>
</html>
'''

db.close()
