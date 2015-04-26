#!/usr/bin/python

import MySQLdb
import os
import cgi, os
import cgitb; cgitb.enable()

db = MySQLdb.connect(host="localhost", 
                     user="root",
                      passwd="3308", 
                      db="RT")
cur = db.cursor() 
cur.execute("SELECT * FROM tracks")



print'''
<html>
<head>
<title>Project RazzTunes</title>
<style type="text/css">
 html{ 
  background: url(../images/bg.jpg) no-repeat center center fixed;  <!-- Photo License: Creative Commons, https://www.flickr.com/photos/elpatojo/216014671/ -->
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  font-family: "Arial", sans-serif;	

    }
    
img{
    opacity: 0.5;
    filter: alpha(opacity=50); 
   }

img:hover{
    opacity: 1.0;
    filter: alpha(opacity=100); 
         }
         
div.playlistFormat{
	  opacity: 0.5;
	  filter: alpha(opacity=50); 
                  }
footer{
   position:absolute;
   height:50px;
      }

</style>

<link rel="shortcut icon" href="/images/play.png" />

</head>
<body>
	<center>
	<h1>Project RazzTunes</h1>
	<div class="playlistFormat">
    <select size=9 id="selectBox" onchange="audioChooser();">
    '''    
    
for row in cur.fetchall() :
	
	print"""<option value='""",row[4],"""'>"""
	

	print row[1],row[2],row[3],row[4]

print'''
	</div>
	<br>
    </select>
	</center>

<script type="text/javascript">
var audio = new Audio;
function audioChooser(){
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
<img src="../images/play.png" onclick="playAudio()" value="Play">
<img src="../images/pause.png" onclick="pauseAudio()" value="Pause">
<img src="../images/stop.png" onclick="stopAudio()" value="Stop">
<br>
<input type="checkbox" onclick="loopAudio()" value="Loop"> Repeat
</center>

<center>
<form enctype="multipart/form-data" action="fileUpload.py" method="post">
<input type="file" name="file">
<button type="submit" style="background:transparent; border:none; color:transparent;"><img src="../images/upload.png"/></button>
</form>

<p style="position: absolute; bottom: 0; width: 100%; text-align: center;">
<a href="https://github.com/stge0958/RT">
<img src="../images/info.png">
</a>
</p></center>

</body>
<footer>



</footer>
</html>
'''
db.close()
