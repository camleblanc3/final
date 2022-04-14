from flask_wtf import FlaskForm 
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class chartForm(FlaskForm):
    chartType = SelectField('Chart Type Selection...', choices=[('pts', 'Points Per Game'), ('reb','Rebounds Per Game'), ('ast','Assists Per Game'), ('stl', 'Steals Per Game'), ('blk', 'Blocks Per Game'), ('fg%', 'Field Goal Percentage'), ('3p%', '3-Point Percentage')], validators=[DataRequired()])
    submit = SubmitField()