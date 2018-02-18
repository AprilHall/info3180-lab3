from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask import Flask, render_template, flash, session, redirect, url_for

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

class User_form(FlaskForm):
	name = StringField('Enter your full name',validators = [DataRequired()])
	email = StringField('Enter your email address',validators = [DataRequired()])
	subject = StringField('Enter the subject of your message',validators = [DataRequired()])
	message = TextAreaField('Please enter your message',validators = [DataRequired()])
	button = SubmitField('Send')
