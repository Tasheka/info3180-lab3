from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
from wtforms import SubmitField, TextAreaField

class MyForm(FlaskForm):
    name=StringField('Name:', validators=[DataRequired()])
    email_address=StringField('Email Address:', validators=[DataRequired()])
    subject=StringField('Subject:', validators=[DataRequired()])
    message=TextAreaField('Message:', validators=[DataRequired()])