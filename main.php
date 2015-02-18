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

<input type="button" onclick="pauseAudio()" value="Pause">
<input type="button" onclick="playAudio()" value="Play">
<input type="button" onclick="nextAudio()" value="Next">





</body></html>


