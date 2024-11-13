from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from flask_wtf.file import FileAllowed, FileRequired, MultipleFileField

class UploadForm(FlaskForm):
    images = MultipleFileField('Select Images', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])
    language = SelectField('OCR Language', choices=[
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('mr', 'Marathi'),
        ('kn', 'Kannada'),
        ('te', 'Telugu'),
        ('ta', 'Tamil'),
    ])
    submit = SubmitField('Upload and Extract Text')
