from app import app

from flask import render_template

@app.route('/')
def home():
    westas = ['lebron james', 'stephen curry', 'andrew wiggins', 'ja morant', 'nikola jokic', 'devin booker', 'rudy gobert', 'chris paul', 'draymond green', 'donovan mitchell', 'luka doncic', ' dejounte murray', 'karl-anthony towns']
    eastas = ['kevin durant', 'trae young', 'jayson tatum', 'joel embiid', 'demar derozan', 'giannis antetokounmpo', 'lamelo ball', 'darius garland', 'james harden', 'zach lavine', 'fred vanvleet', 'jimmy butler', 'khris middleton', 'jarrett allen']
    return render_template('index.html', westas = westas, eastas = eastas)