from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY']='iMawesome'
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT']='2525'
app.config['MAIL_USERNAME']='bcffb23030078a'
app.config['MAIL_PASSWORD']='9fec4948c3af45'

mail=Mail(app)
from app import views