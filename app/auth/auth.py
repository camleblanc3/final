from flask import Blueprint, session, redirect, render_template, request, url_for, flash

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')
import pyrebase

config = {
    'apiKey': "AIzaSyCkp48LWfqzYZqJYai7Um0iCj9ziO4SkrU",
    'authDomain': "final-5da16.firebaseapp.com",
    'projectId': "final-5da16",
    'storageBucket': "final-5da16.appspot.com",
    'messagingSenderId': "925408783056",
    'appId': "1:925408783056:web:616c02aab4114cf56f4cd5",
    'measurementId': "G-SL6VMP3Y70",
    'databaseURL': ''
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@auth.route('/', methods=['GET','POST'])
def signin():
    if('user' in session):
        return 'Hello,{}'.format(session['user'])
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            session['user'] = email
        except:
            return 'Failed to login'
    
    return render_template('signin.html')

@auth.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')
