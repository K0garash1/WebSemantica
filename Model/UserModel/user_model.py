import psycopg2

conexion = None
pg_username = 'postgres'
pg_password = 'root'

def query_user(email):
    try:
        conexion = psycopg2.connect(
            f"dbname=postgres user={pg_username} password={pg_password}"
        )
        cur = conexion.cursor()
        cur.execute(
            f"SELECT U.password FROM user U WHERE lower(U.email)={email}"
        )
        user = cur.fetchone()
        return user
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
