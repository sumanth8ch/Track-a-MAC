<?php
   include('config.php');
   $sql =<<<EOF
	INSERT INTO manager (ip,port,community,version) VALUES ("$_GET[ip]","$_GET[port]","$_GET[community]","$_GET[version]");
EOF;
   $answer = $db->exec($sql);
   if(!$answer){
      echo "FALSE";
   }else{
	echo "OK";
}

   $db->close();
?>
