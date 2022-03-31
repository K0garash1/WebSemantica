'''
Proyecto de curso - Fundamentos de ingenieria de Software
Servidor flask encargado de administrar las peticiones del usuario y desplegar las vistas correspondientes
Para su ejecucion es necesario contar con python3 instalado en el sistema y ejecutar el script de insralacion
En Linux desde una terminal bash: ./run.sh
En Windows desde una terminalPowerShell: .\run.bat
El script creará el entorno virtual de python e instalara en el los paquetes necesarios
por lo que se requiere estar conectado a internet para su ejecucion
'''
import sys
from flask import Flask, redirect, render_template, request, request_finished, url_for, session;
sys.path.append('Controllers/UserController')
from user_controller import user_login, user_logout
sys.path.append('Controllers/DataController')
from data_controller import send_query

'''
Configuracion de la aplicacion
Se esyablecen los directorios para los recursos web, en este caso el paquete vista, que cuenta
con las vistas de usuario y administrador
SECRET_KEY establece la clave secreta de la aplicacion
SERVER_NAME establece la ip y el puerto en la que será desplegado el servidor
'''
app=Flask(__name__, template_folder="Views", static_folder="Views")
app.config['SECRET_KEY'] = 'secret'
app.config['SERVER_NAME'] = '127.0.0.1:5000'

'''
Vista pincipal de usuario que desplegara la interfaz de consulta de REA y capturará los datos
ingresados para procesarlos en el paquete DataContoller
'''
@app.route("/", methods=['GET', 'POST'])
def home():
    #Recibe la consulta del usuario y gestiona la respuesta
    if request.method == 'POST':
        tripleta = send_query(request.form)
        return redirect(url_for('viewInfo', info = tripleta))
    #Despliega formulario de consulta
    else:
        return render_template("UserView/view.html")

'''
Vista de presentacion de la informacion recuperada mediante la consulta RDF
El usuario es redirigido automaticamente cuando el servidor Fuseki genera una respuesta, la 
cual es almacenada en el parametro de la peticion 'info'
'''
@app.route("/viewInfo")
def viewInfo():
    return render_template("UserView/viewInfo.html", info=request.args.get('info'))
    
'''
Vista de ayuda al usuario, ofrece un manual para el uso de la interfaz de consulta
'''
@app.route("/help")
def help():
    return render_template("UserView/help.html")

'''
Vista de administrador, requiere de tener una sesion activa
desde la misma se pordrá acceder a la configuracion del servidor Tomcat/Fuseki y a la de
DSpace
'''
@app.route("/admin")
def admin():
    #En caso de tener una sesion activa accesa a la vista del adminostrador
    if 'loggedin' in session:
        return render_template("AdminView/view.html")
    #En caso de no tener una sesion redirije a la vista para el inicio de sesion
    else:
        return redirect(url_for('login'))

'''
Vista para el inicio de sesion para administradores
Ofrece un formulario simple con los campos email y contraseña que serán validados en
la base de datos postgresql
'''
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
