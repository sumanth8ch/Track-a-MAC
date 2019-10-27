
<?php
   include('config.php');
  $sql =<<<EOF
	DELETE from manager where ip = "$_GET[ip]";
EOF;
   $answer = $db->exec($sql);
   if(!$answer){
      echo "FALSE";
   }else{
	echo "OK";
}

   $db->close();
?>
