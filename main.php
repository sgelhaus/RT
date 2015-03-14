<html>
<head>
 
<?php
$connect = mysql_connect('127.0.0.1', 'root', '');
mysql_select_db("RT");
$query = "SELECT * FROM tracks";
$result = mysql_query ($query);
?>
						<form id='trackList'>
                        <select size=3>
                        <?php
                        while($output=mysql_fetch_assoc($result)){
                        ?>
                        <option id=<?php echo $output[Id]; ?> value=<?php echo $output[Id]; ?> onclick=audioHandler()><?php echo $output[Id]; ?> <?php echo $output[Title]; ?> <?php echo $output[Artist]; ?> <?php echo $output[FileName]; ?></option>

						<?php
                        }
                        ?>
                        </select>
                        </form>
<?php                                        
mysql_free_result($result);
?>






<script type="text/javascript">
var audio = new Audio;
function audioHandler() {
var ID = document.getElementById('<?php echo $output[Id]; ?>').value 
alert(ID)


<?php
$num=$output[Id];
$connect = mysql_connect('127.0.0.1', 'root', '');
mysql_select_db("RT");
$query1 = "SELECT FileName FROM tracks where Id=$num";
$result1 = mysql_query($query1);
$output1=mysql_fetch_assoc($result1);
mysql_free_result($result1);
?>
	audio.setAttribute("src", '<?php echo "./audio/" . $output1[FileName]; ?>');
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



<form enctype="multipart/form-data" action="upload.php" method="POST">
<input type="hidden" name="MAX_FILE_SIZE" value="10000000" />
Choose a file to upload: <input name="uploadedfile" type="file" /><br />
<input type="submit" value="Upload File" />
</form>




</body></html>
