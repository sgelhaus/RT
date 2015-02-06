<!DOCTYPE html>
<html>
<body>

<h1>Example Heading</h1>
<p>Example below.</p>


<SELECT NAME="TrackList" style="width:400px" MULTIPLE>
<OPTION> Track 1
<OPTION> Track 2
<OPTION> Track 3
<OPTION> Track 4
<OPTION> Track 5
</SELECT>


<p>
<p>

<SELECT NAME="test" style="width:400px" size="6" MULTIPLE>
<?php
if ($open = opendir('./audio')) {
    #while (false !== ($file = readdir($open))) {
    while ($file = readdir($open)) {
    	if ($file !== ".." && $file !== "."){
            echo "<OPTION value=$file>$file</OPTION>";
              }
           }
    closedir($open);
}
?>
</SELECT>

<p>
<p>
<p>

<form action="upload.php" method="post" enctype="multipart/form-data">
    Select image to upload:
    <input type="file" name="fileToUpload" id="fileToUpload">
    <input type="submit" value="Upload Image" name="submit">
</form>

<p>
<p>
<p>


<audio id="myAudio"
 <source src="./audio/1.mp3"
         type='audio/mp3'>
 Your browser is not supported.
</audio>
<button type="button" onclick="aud_play_pause()">Play/Pause</button>
<script>
function aud_play_pause() {
  var myAudio = document.getElementById("myAudio");
  if (myAudio.paused) {
    myAudio.play();
  } else {
    myAudio.pause();
  }
}
</script>


</body>
</html> 