import sys
sys.path.insert(1, 'Model/UserModel')
from user_model import query_user

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

def user_logout(session):
    session.pop('loggedin', None)
    session.pop('email', None)
    session.pop('password', None)
