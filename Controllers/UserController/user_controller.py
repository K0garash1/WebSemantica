'''
Controlador de usuarios
Se encarga de administrar los datos de acceso para la sesion de un
usuario tipo administrador
'''
import sys
sys.path.insert(1, 'Model/UserModel')
from user_model import query_user

'''
Modulo de inicio de sesion, recive un formulario con los campos 'email' y 'password'
Busca al usuario por email en la base de datos y compara las contraseñas
Si coinciden se establece una sesion activa
Si no coinciden se elimina la sesion
'''
def user_login(session, form):
    email = form['email']
    password = form['password']
    user = query_user(email)
    if user[1] == password:
        session['email']=user[0]
        session['password']=user[1]
        session['loggedin']=True
    else:
        session.pop('loggedin', None)

'''
Cierre de sesion
Limpia los campos dela sesion actual y desactiva el estado 'loggedin'
'''
def user_logout(session):
    session.pop('loggedin', None)
    session.pop('email', None)
    session.pop('password', None)
