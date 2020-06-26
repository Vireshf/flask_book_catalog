from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField
from wtforms.validators import DataRequired, Email, Length,ValidationError,EqualTo
from app.auth.models import User

def email_exists(form,field):
	email = User.query.filter_by(user_email=field.data).first()
	if email:
		raise ValidationError('Email already exists')


class RegistrationForm(FlaskForm):
    name = StringField('Enter your name',validators=[DataRequired(),Length(3,15, message='should be between 3 to 15 characters')])
    email = StringField('Enter your Email',validators=[DataRequired(),Email(),email_exists])
    password = PasswordField('Enter your Password',validators=[DataRequired(),Length(5),EqualTo('confirm',message='password should match')])
    confirm = PasswordField('Confirm the password',validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
	email = StringField('Enter your Email',validators=[Email(),DataRequired()])
	password = PasswordField('Enter your password',validators=[DataRequired(),Length
		(3,15,message='should be between 3 to 15 characters')])
	remember_me = BooleanField('remember_me')
	submit = SubmitField('Login')