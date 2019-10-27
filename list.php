<?php
  include('config.php');

   $sql =<<<EOF
      SELECT * from finalproject;
EOF;

   $ret = $db->query($sql);
   while($row = $ret->fetchArray(SQLITE3_ASSOC) ) {
      echo   $row['IPADDRESS']." | ".$row['VLAN']." | ".$row['PORT']." | ".$row['MACS']."\n";
   }

   $db->close();
?>
