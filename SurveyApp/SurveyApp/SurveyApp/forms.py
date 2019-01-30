import email

from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, PasswordField, SelectField, \
    StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp, \
    ValidationError, url
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from .models import User


class AddNoteForm(FlaskForm):
	title = StringField('title', validators=[DataRequired()])
	content = TextAreaField('content', validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = StringField('Your email: ', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField()

class SignupForm(FlaskForm):
	username = StringField('Username',
							validators=[
							DataRequired(), Length(3, 80),
							#Regexp('^[A-Za-z0-9_]{3,}S',
							#	message='Usernames consist of numbers, letters,''and underscores.')
							])
	password = PasswordField('Password',
					validators=[
					DataRequired(),
					EqualTo('password2', message='Passwords must match.')])
	password2 = PasswordField('Confirm Password', validators=[DataRequired()])
	email = StringField('Email',
				validators=[DataRequired(), Length(1, 120), Email()])

	def validate_email(self, email_field):
		if User.query.filter_by(email=email_field.data).first():
			raise ValidationError('There is already a user with this email address.')

	def validate_username(self, username_field):
		if User.query.filter_by(username=username_field.data).first():
			raise ValidationError('This username is already taken')

class surveyForm(FlaskForm):
	name = StringField('name',
							validators=[
							DataRequired(), Length(3, 50),
							#Regexp('^[A-Za-z0-9_]{3,}S',
							#	message='Names consist of letters.')
							])
	nationality = StringField('nationality', validators=[DataRequired()])
	gender = StringField('gender', validators=[DataRequired()])
	age = StringField('age', validators=[DataRequired()])
	
class argumentsForm(FlaskForm):
	side = StringField('side', validators=[DataRequired()])
	title = StringField('title', validators=[DataRequired()])
	claim = StringField('claim', validators=[DataRequired()])
	
class ratesForm(FlaskForm):
	strength = StringField('Strenght', validators=[DataRequired()])
	Why = StringField('why', validators=[DataRequired()])

