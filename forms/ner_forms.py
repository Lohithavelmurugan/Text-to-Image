
from flask_wtf import FlaskForm
from wtforms import SubmitField

class NERForm(FlaskForm):
    submit = SubmitField('Perform Named Entity Recognition')
