#import os
from sqlalchemy import create_engine
import cx_Oracle
import pylint

#Datos de conexion de la BD Siebel
host='172.21.31.10'
port='1522'
db='CVSIEBEXRAC'
user='SOP_P-JJGALICIA'
password='O@SeRap8EBRO'
# host='172.21.61.8'
# port='1521'
# db='servicearcadia'
# user='LEQUIPOS_OWNER'
# password='Otr0_.P4sSNu3v0_'

#Creacion del engine para conexion a la BD
engine = create_engine('oracle+cx_oracle://' + user + ':' + password + '@' + host + ':' + port + '/?service_name=' + db)

##engine = sqlalchemy.create_engine('oracle+cx_oracle://' + user + ':' + password + '@' + host + ':' + port + '/?service_name=' + sid)
result = engine.execute('SELECT sysdate from dual')
for row in result:
    print (row)


def isUserValid( username, password ):
    result = engine.execute("SELECT sysdate from dual")
    if result is not None:
        return True
    return False