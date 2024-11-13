
from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField

class FunctionalityForm(FlaskForm):
    functionality = RadioField('Select Functionality', choices=[
        ('extract', 'Extract Text from Image'),
        ('translate', 'Translate Extracted Text'),
        ('ner', 'Perform Named Entity Recognition'),
        ('all', 'All of the Above')
    ], default='extract')
    submit = SubmitField('Proceed')
