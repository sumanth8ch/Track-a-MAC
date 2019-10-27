<?php
  include('config.php');
$searchstr = $_GET[mac];
   $sql =<<<EOF
      SELECT * from finalproject WHERE MACS LIKE "%$searchstr%"  ORDER BY MACS ;
EOF;

   $ret = $db->query($sql);
   while($row = $ret->fetchArray(SQLITE3_ASSOC) ) {
      echo   $row['IPADDRESS']." | ".$row['VLAN']." | ".$row['PORT']." | "."$searchstr"."\n";
   }

   $db->close();
?>
