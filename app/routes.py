
import json
from app import app
from flask import session, redirect, render_template, request, url_for, flash
from firebase import firebase
import plotly
import plotly.express as px
import pandas as pd
from .forms import chartForm, compareForm, lineupForm
import pyrebase
from .authforms import SignInForm, RegisterForm



@app.route('/')
def home():
    westas = ['lebron james', 'stephen curry', 'andrew wiggins', 'ja morant', 'nikola jokic', 'devin booker', 'rudy gobert', 'chris paul', 'draymond green', 'donovan mitchell', 'luka doncic', ' dejounte murray', 'karl-anthony towns']
    eastas = ['kevin durant', 'trae young', 'jayson tatum', 'joel embiid', 'demar derozan', 'giannis antetokounmpo', 'lamelo ball', 'darius garland', 'james harden', 'zach lavine', 'fred vanvleet', 'jimmy butler', 'khris middleton', 'jarrett allen']
    
    
    return render_template('index.html', westas = westas, eastas = eastas)

fb = firebase.FirebaseApplication('https://final-5da16-default-rtdb.firebaseio.com/', None)
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
@app.route('/cards')
def cards():
    pc = fb.get('/players',None)
   
    return render_template('cards.html', pc = pc)

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




@app.route('/stats', methods=['POST','GET'])
def stats():
    form = chartForm()
    f = form.statType.data
    c = form.chartType.data
    x= {'pts':'Points Per Game', 'per':'Player Efficiency Rating', 'reb':'Rebounds Per Game', 'ast':'Assists Per Game', 'stl':'Steals Per Game', 'blk':'Blocks Per Game', 'fg%':'Field Goal Percentage', '3p%':'3-Point Percentage'}
    if request.method == 'POST':
        if c == 'Scatter-Plot':
            try:
                stat = fb.get('/players',None)
                st = pd.DataFrame(stat)
                fig = px.scatter(st, x='last_name', y=f'{f}',title=f'{x[f]}', labels={'last_name': 'Players', f'{f}' : f'{x[f]}'} )
                graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            except:
                stat = fb.get('/players',None)
                st = pd.DataFrame(stat)
                fig = px.scatter(st, x='last_name', y='pts' )
                graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        elif c == 'Bar-Graph':
            try:
                stat = fb.get('/players',None)
                st = pd.DataFrame(stat)
                fig = px.bar(st, x='last_name', y=f'{f}',title=f'{x[f]}', labels={'last_name': 'Players', f'{f}' : f'{x[f]}'},)
                graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            except:
                stat = fb.get('/players',None) 
                st = pd.DataFrame(stat)
                fig = px.bar(st, x='last_name', y='pts' )
                graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        else:
            try:
                stat = fb.get('/players',None)
                st = pd.DataFrame(stat)
                fig = px.line(st, x='last_name', y=f'{f}',title=f'{x[f]}', labels={'last_name': 'Players', f'{f}' : f'{x[f]}'} )
                graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            except:
                stat = fb.get('/players',None)
                st = pd.DataFrame(stat)
                fig = px.line(st, x='last_name', y='pts' )
                graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        
            
        return render_template('stats.html',form=form,  graphJSON=graphJSON)
    
    return render_template('stats.html',form=form, graphJSON=None)

@app.route('/compare', methods=['GET','POST'])
def compare():
    form=compareForm()
    p1 = form.player1.data
    p2 = form.player2.data
    p3 = form.player3.data
    p4 = form.player4.data
    p5 = form.player5.data
    p = [f'{p1}',f'{p2}',f'{p3}',f'{p4}',f'{p5}'] 
    s = form.statType.data
    gh = {'pts':'Points Per Game', 'per':'Player Efficiency Rating' , 'reb':'Rebounds Per Game', 'ast':'Assists Per Game', 'stl':'Steals Per Game', 'blk':'Blocks Per Game', 'fg%':'Field Goal Percentage', '3p%':'3-Point Percentage'}
    players = {'Embiid': 'Joel Embiid', 'Antetokounmpo': 'Giannis Antetokounmpo', 'Doncic': 'Luka Doncic', 'Young': 'Trae Young', 'DeRozan': 'DeMar DeRozan', 'Jokic': 'Nikola Jokic', 'Tatum': 'Jayson Tatum', 'Booker': 'Devin Booker', 'James': 'LeBron James', 'Durant': 'Kevin Durant', 'Gobert': 'Rudy Gobert', 'Morant': 'Ja Morant', 'Towns': 'Karl-Anthony Towns', 'Allen': 'Jarrett Allen', 'Curry': 'Stephen Curry', 'Paul': 'Chris Paul', 'Harden': 'James Harden', 'Murray': 'Dejounte Murray', 'Garland': 'Darius Garland', 'Ball': 'Lamelo Ball', 'Wiggins': 'Andrew Wiggins', 'Green': 'Draymond Green', 'Lavine': 'Zach Lavine', 'VanVleet': 'Fred VanVleet', 'Butler': 'Jimmy Butler', 'Middleton': 'Khris Middleton', 'Mitchell': 'Donovan Mitchell'}
    if request.method == 'POST':
        try:
            k = []
            stat = fb.get('/players',None)
            for x in stat:
                if x['last_name'] in p:
                    k.append(x)
            st = pd.DataFrame(k)
            fig = px.histogram(st, x='last_name', y=f'{s}', labels={'last_name': 'Players', f'{s}' : f'{gh[s]}'}, color='last_name')
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        except:
            stat = fb.get('/players',None)
            st = pd.DataFrame(stat)
            fig = px.line(st, x='last_name', y='pts')
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        
        return render_template('compare.html',form=form,  graphJSON=graphJSON)
    
    return render_template('compare.html',form=form, graphJSON=None)

@app.route('/lineup', methods=['GET','POST'])
def lineup():
    form = lineupForm()
    p1 = form.player1.data
    p2 = form.player2.data
    p3 = form.player3.data
    p4 = form.player4.data
    p5 = form.player5.data
    p = [f'{p1}',f'{p2}',f'{p3}',f'{p4}',f'{p5}'] 
    if request.method == 'POST':
        try:
            k = []
            stat = fb.get('/players',None)
            for x in stat:
                if x['last_name'] in p:
                    k.append(x)
        except:
            pass    
        return render_template('lineup.html', form=form, k=k)
    return render_template('lineup.html', form=form)

    
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


