'''
Modelo de administracion de usuarios
'''
import psycopg2

#Datos de acceso a la base de datos Postgresql
conexion = None
pg_username = 'postgres'
pg_password = 'root'

#Consulta un usuario en la base de datos mediante la busqueda de su email
def query_user(email):
    try:
        #Conecta con la base de datos
        conexion = psycopg2.connect(
            f"dbname=postgres user={pg_username} password={pg_password}"
        )
        cur = conexion.cursor()
        #Consulta en la base de datos
        cur.execute(
            f"SELECT U.password FROM user U WHERE lower(U.email)={email}"
        )
        #Selecciona el primer resultado y lo retorna
        user = cur.fetchone()
        return user
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        #Cierra conexion con la base de datos
        if conexion is not None:
            conexion.close()
