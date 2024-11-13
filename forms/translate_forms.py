
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField

class TranslateForm(FlaskForm):
    target_language = SelectField('Translate to', choices=[
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('mr', 'Marathi'),
        ('kn', 'Kannada'),
        ('te', 'Telugu'),
        ('ta', 'Tamil'),
    ])
    submit = SubmitField('Translate')
