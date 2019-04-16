from sqlalchemy import create_engine
import cx_Oracle


#Datos de conexion de la BD que se quiere accesar 
db_user='LEQUIPOS_OWNER'
db_password='Otr0_.P4sSNu3v0_'
db_host='172.21.61.8'
db_port='1521'
service_name='servicearcadia'
sid=''

#Creacion del adaptador de conexion a la BD cuando la base usa SID 
#engine = create_engine('oracle://'+ user + ':' + pw + '@' + hostname + ':' + port + '/' + sid)
#Creacion del adaptador de conexion a la BD cuando la base usa service name
#engine = create_engine('oracle+cx_oracle://' + user + ':' + pw + '@' + host + ':' + port + '/?service_name=' + service_name)
#sqlalchemy.engine.url.URL("oracle", db_user, db_password, service_name)


#Creacion del engine para llevar a cabo las peticiones a la base de datos agregando parametros adicionales aparte del connection string
engine = create_engine('oracle+cx_oracle://' + db_user + ':' + db_password + '@' + db_host + ':' + db_port + '/?service_name=' + service_name)

#Proceso de validacion del usuario en la base de datos 
def isUserValid( username, password ):
    result = engine.execute("SELECT ID from USUARIOS_IW where USER_NAME ='{0}' AND PASSWORD = '{1}'".format(username, password))
    valid = 0
    for row in result:
            valid = 1 
            print (row)
                 
    if valid ==1:
            print ("Usuario Valido")
            return True
    else:
            print ("Usuario o Password no Validos")
            print (valid)
            return False
        





