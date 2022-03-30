from crypt import methods
import sys
from urllib.request import Request;
from flask import Flask, redirect, render_template, request, request_finished, url_for, session;
sys.path.append('Controllers/UserController')
from user_controller import user_login, user_logout
sys.path.append('Controllers/DataController')
from data_controller import send_query


app=Flask(__name__, template_folder="Views", static_folder="Views")
app.config['SECRET_KEY'] = 'secret'

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tripleta = send_query(request.form)
        return redirect(url_for('viewInfo', info = tripleta))
    else:
        return render_template("UserView/view.html")

@app.route("/viewInfo")
def viewInfo():
    return render_template("UserView/viewInfo.html", info=request.args.get('info'))
    

@app.route("/help")
def help():
    return render_template("UserView/help.html")

@app.route("/admin")
def admin():
    if 'loggedin' in session:
        return render_template("AdminView/view.html")
    else:
        return redirect(url_for('login'))

@app.route("/login", methods=['POST', 'GET'])
def login():
    if 'loggedin' in session:
        return redirect(url_for('admin'))
    else:
        if request.method == 'POST':
            user_login(session, request.form)
            return redirect(url_for('admin'))
        else:
            return render_template("AdminView/login.html")

@app.route("/logout")
def logout():
    if 'loggedin' in session:
        user_logout(session)    
    return redirect(url_for('login'))