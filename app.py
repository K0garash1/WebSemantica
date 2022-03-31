#Servidor flask encargado de administrar las peticiones del usuario

import sys
from flask import Flask, redirect, render_template, request, request_finished, url_for, session;
sys.path.append('Controllers/UserController')
from user_controller import user_login, user_logout
sys.path.append('Controllers/DataController')
from data_controller import send_query

#Establece los directorios para la obtencion de recursos
app=Flask(__name__, template_folder="Views", static_folder="Views")
app.config['SECRET_KEY'] = 'secret'

#Pagina de inicio, despliega la vista de usuario y pone a disposicion del usuario una interfaz de consulta
@app.route("/", methods=['GET', 'POST'])
def home():
    #Recibe la consulta del usuario y gestiona la respuesta
    if request.method == 'POST':
        tripleta = send_query(request.form)
        return redirect(url_for('viewInfo', info = tripleta))
    #Despliega formulario de consulta
    else:
        return render_template("UserView/view.html")

#Vista de la respuesta, presenta la informacion recuperada
@app.route("/viewInfo")
def viewInfo():
    return render_template("UserView/viewInfo.html", info=request.args.get('info'))
    
#Ayuda al usuario
@app.route("/help")
def help():
    return render_template("UserView/help.html")

#Vista de administrador
@app.route("/admin")
def admin():
    #En caso de tener una sesion activa accesa a la vista del adminostrador
    if 'loggedin' in session:
        return render_template("AdminView/view.html")
    #En caso de no tener una sesion redirije a la vista para el inicio de sesion
    else:
        return redirect(url_for('login'))

#Vista para el inicio de sesion para administradores
@app.route("/login", methods=['POST', 'GET'])
def login():
    #En caso de que ya exista una sesion redirije a la vista de administrador
    if 'loggedin' in session:
        return redirect(url_for('admin'))
    #En caso de no tener una sesion iniciada administra la peticion del usuario
    else:
        #Si el usuario ingresó datos para el acceso accesa a la base de datos e intenta iniciar sesion
        if request.method == 'POST':
            user_login(session, request.form)
            return redirect(url_for('admin'))
        #En caso de que el usuario este solicitando la vista para el ingreso de datos
        else:
            return render_template("AdminView/login.html")

#Cierra la sesion activa
@app.route("/logout")
def logout():
    if 'loggedin' in session:
        user_logout(session)    
    return redirect(url_for('login'))
