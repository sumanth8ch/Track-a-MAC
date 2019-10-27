<?php
  include('config.php');
   $sql =<<<EOF
      SELECT * from manager;
EOF;

   $ret = $db->query($sql);
   while($row = $ret->fetchArray(SQLITE3_ASSOC) ) {
      echo   $row['ip']." | ".$row['port']." | ".$row['community']." | ".$row['version']." | ".$row['firstprob']."| ".$row['lastprob']."\n";
   }

   $db->close();
?>
