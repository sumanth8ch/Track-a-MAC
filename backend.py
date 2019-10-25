#!/usr/bin/env python

from easysnmp import Session
import  sqlite3
import time

vl = "DEFAULT_VLAN(1)"

while True:
 database = sqlite3.connect('ourdb.db')
 details = database.execute("select * from manager")
 for i in details:
  ipaddress = i[0]
  port = i[1]
  community = i[2]
  version = i[3]
  try:
   session = Session(hostname=ipaddress,port=port, community=community, version=2,timeout=5,retries=2)
   macs     = session.walk('.1.3.6.1.2.1.17.4.3.1.1')
   ports = session.walk('.1.3.6.1.2.1.17.4.3.1.2')
  except:
   print "timeout"
   continue
  starttime = time.time()
  finishtime=time.ctime(int(starttime))
  print "ok"

  for x,y in zip(macs,ports):
         oid=x.oid
         oid_index=x.oid_index
         snmp_type=x.snmp_type
         mac=':'.join('{:02x}'.format(ord(i)) for i in x.value)
         portvalue =y.value

         data = database.execute("SELECT * from finalproject where (PORT =? AND IPADDRESS=?)", (portvalue,ipaddress,))
         rows = data.fetchall()
         for i in rows:
           k = i[3]
         if len(rows)==0:
           database.execute(''' INSERT INTO finalproject(IPADDRESS,VLAN,PORT,MACS) VALUES(?,?,?,?)''', (ipaddress,vl,portvalue,mac))
           database.commit()
         elif len(rows)==1 and k.find(mac) is -1:
           endmac=k+","+mac
           database.execute("UPDATE finalproject set MACS=? where PORT = ?",(endmac,portvalue,))
           database.commit()
  database.execute("UPDATE manager set firstprob=?, lastprob=? where ip = ?",(finishtime,finishtime,ipaddress,))
  database.commit()


  vlansnum = []
  vlanname = []
  vlans  = session.walk('.1.3.6.1.2.1.17.7.1.4.3.1.4')
  vlanindex=session.walk('.1.3.6.1.2.1.17.7.1.4.3.1.1')
  values=[]
  oids=[]
  for x,y in  zip(vlanindex,vlans):
     value= ':'.join('{:02x}'.format(ord(i)) for i in x.value)
     values=value.split(":")
     oid=x.oid
     oids.append(oid)
     vname=y.value
     vnums = oid.split('.')
     vnum =str(vnums[-1])
     temp = ''
     if vname != "DEFAULT_VLAN":
         for i in range(len(values)):
             list = values
             val = list[i]
             scale = 16
             numofbits=8
             vals = bin(int(val, scale))[2:].zfill(numofbits)
             temp = temp + str(vals)
             vals = ''
             listvals = list(combine)
         for i in range(len(listvals)):
             if listvals[i] == '1':
                 x = i +1
                 vlanname.append(str(vname)+"("+vnum+")")
                 vlansnum.append(x)

  for i in range(len(vlansnum)):
      portlan = "1"
      database.execute(""" UPDATE finalproject SET VLAN = ?  where PORT = ? """, (vlanname[i],vlansnum[i]))
      database.commit()
 database.close
 time.sleep(60)
