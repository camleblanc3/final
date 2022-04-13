import json
from app import app

from flask import session, redirect, render_template, request, url_for, flash, jsonify
from firebase import firebase
import plotly
import plotly.express as px

@app.route('/')
def home():
    westas = ['lebron james', 'stephen curry', 'andrew wiggins', 'ja morant', 'nikola jokic', 'devin booker', 'rudy gobert', 'chris paul', 'draymond green', 'donovan mitchell', 'luka doncic', ' dejounte murray', 'karl-anthony towns']
    eastas = ['kevin durant', 'trae young', 'jayson tatum', 'joel embiid', 'demar derozan', 'giannis antetokounmpo', 'lamelo ball', 'darius garland', 'james harden', 'zach lavine', 'fred vanvleet', 'jimmy butler', 'khris middleton', 'jarrett allen']
    return render_template('index.html', westas = westas, eastas = eastas)

fb = firebase.FirebaseApplication('https://final-5da16-default-rtdb.firebaseio.com/', None)

@app.route('/cards')
def cards():
    pc = fb.get('/players',None)
    return render_template('cards.html', pc = pc)


@app.route('/stats')
def stats():
    stat = fb.get('/players',None)
    st = px.data.stat()
    fig = px.bar(st, x='last_name', y='pts')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('stats.html', graphJSON=graphJSON)


import pyrebase
from .authforms import SignInForm, RegisterForm

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


@app.route('/register', methods=['GET','POST'])
def register():
    rform = RegisterForm()
    if request.method == 'POST':
        email = rform.email.data
        password = rform.password.data
        try:
            user = auth.create_user_with_email_and_password(email,password)
            user = auth.sign_in_with_email_and_password(email,password)
            session['user'] = email
            flash(f'Successfully registered! Welcome, {rform.email.data}!', category='success')
        except:
            flash(f'That username or email is taken. Please try a different one.', category='danger')
            return redirect(url_for('register'))
        return redirect(url_for('home'))
    return render_template('register.html', rform = rform)


@app.route('/signin', methods=['GET','POST'])
def signin():
    siform = SignInForm()
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            session['user'] = email
            
            flash(f'Welcome back, {siform.email.data}!')
        except:
            flash(f'Login failed, incorrect username or password.', category='danger')
        return redirect(url_for('home'))
    
    return render_template('signin.html', siform = siform)

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')


