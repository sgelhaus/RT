<html>
<head>
 
<?php
$connect = mysql_connect('127.0.0.1', 'root', '');
mysql_select_db("RT");
$query = "SELECT * FROM tracks";
$result = mysql_query ($query);
						echo "<form id='trackList'>";
                        echo "<select size=3 onclick=audioHandler()>";
                        while($output=mysql_fetch_assoc($result)){
                        echo "<option id=$output[Id] value=$output[Id]>$output[Id] $output[Title] $output[Artist] $output[FileName]</option>";
                        
                        }
                        
                        echo "</select>";
                        echo "</form>";
                                        
mysql_free_result($result);
?>




<script type="text/javascript">
var audio = new Audio;
function audioHandler() {
<?php
$num=1;
$connect = mysql_connect('127.0.0.1', 'root', '');
mysql_select_db("RT");
$query = "SELECT FileName FROM tracks where Id=$num";
$result = mysql_query($query);
$output=mysql_fetch_assoc($result);
mysql_free_result($result);
?>
	audio.setAttribute("src", '<?php echo "./audio/" . $output[FileName]; ?>');
	audio.load();
	audio.play();
	
}
function pauseAudio() {
    audio.pause();
}
function playAudio(){
    audio.play();
}
function nextAudio(){
	audio.pause();
	
	<?php
	$num=$num+1;
	$connect = mysql_connect('127.0.0.1', 'root', '');
	mysql_select_db("RT");
	$query = "SELECT FileName FROM tracks where Id=$num";
	$result = mysql_query($query);
	$output=mysql_fetch_assoc($result);
	mysql_free_result($result);
	?>
	
	audio.setAttribute("src", '<?php echo "./audio/" . $output[FileName]; ?>');
	audio.load();
	audio.play();
}
</script>
<br>
<input type="button" onclick="pauseAudio()" value="Pause">
<input type="button" onclick="playAudio()" value="Play">
<input type="button" onclick="nextAudio()" value="Next">

<p>



<form enctype="multipart/form-data" action="<?=$_SERVER['PHP_SELF'];?>" method="POST">
<input type="hidden" name="MAX_FILE_SIZE" value="10000000" />
Choose a file to upload: <input name="uploadedfile" type="file" /><br />
<input type="submit" value="Upload File" />
</form>




<?php
$target_path = "./audio/";
$target_path = $target_path . basename( $_FILES['uploadedfile']['name']); 
if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
    echo "The file ".  basename( $_FILES['uploadedfile']['name'])." has been uploaded";
} 
else{
    echo "There was an error uploading the file, please try again!";
}
?>


</body></html>

