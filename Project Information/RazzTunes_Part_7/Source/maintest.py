#!/usr/bin/python

import MySQLdb
import os
import cgi, os
import cgitb; cgitb.enable()
## \file maintest.py Main player functionality is located within this python file

## \brief Project RazzTunes
## \details A web based music player
## \authors Team RazzTunes: Stephen Gelhaus, Parvinder Singh, Dan Sjaastad, Frank Erdesz
## \version beta

## A global variable for database information
db = 0

## A global variable cursor
cur = 0

db = MySQLdb.connect(host="localhost", 
						 user="root", 
						  passwd="3308", 
						  db="RT") 
						  
## @param db Brings database variables into main function						  
def main()

	## A variable for cursor 
	cur = db.cursor() 
	cur.execute("SELECT * FROM tracks") 

	print"""
	<html>
	<head>
	<title>Project RazzTunes</title>
	<style type="text/css">
	 html{ 
	  background: url(../images/bg.jpg) no-repeat center center fixed;  //Photo License: Creative Commons, www.flickr.com/photos/hexidecimal/6673189339
	 // -webkit-background-size: cover;
	 // -moz-background-size: cover;
	 // -o-background-size: cover;
	  background-size: cover;
	}
	 .playlistFormat {
		  color: red;
		  font-size: 2em;
	  }
	 footer {
	   position:absolute;
	   bottom:0;
	   width:100%;
	   height:50px;
	}

	</style>
	</head>
	<body>
		<center>
		<h1>Project RazzTunes</h1>
	
		<select size=9 id="selectBox" onchange="audioChooser();">
		'''    
	
	for row in cur.fetchall() : ;
	
		print"""<option class="playlistFormat" value='""",row[5],"""'>"""
	

		print row[1],row[2],row[3],row[4],row[5]

	print'''
		<br>
		</select>
		</center>

	<script type="text/javascript">
	var audio = new Audio;
	function audioChooser() {
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
	function loopAudio(){
		if(audio.loop){
		audio.loop=false;
		}
		else{
		audio.loop=true;
		}
	}
	</script>

	<br>
	<center>
	<input type="image" src="../images/play.png" onclick="playAudio()" value="Play">
	<input type="image" src="../images/pause.png" onclick="pauseAudio()" value="Pause">
	<input type="image" src="../images/stop.png" onclick="stopAudio()" value="Stop">
	<br>
	<input type="checkbox" onclick="loopAudio()" value="Loop"> Repeat
	</center>

	</body>
	<footer>

	<form enctype="multipart/form-data" action="fileUpload.py" method="post">
	<input type="file" name="file">
	<button type="submit" style="background:transparent; border:none; color:transparent;"><img src="../images/upload.png"/></button>
	</form>

	<p style="position: absolute; bottom: 0; width: 100%; text-align: center;">
	<a href="https://github.com/stge0958/RT">
	<img src="../images/info.png">
	</a>
	</p>

	</footer>
	</html>
	"""
	db.close() 

main(db)
