from flask import render_template, request,flash,redirect,url_for
from flask_login import login_user, logout_user,login_required,current_user
from app.auth.forms import RegistrationForm
from app.auth.forms import LoginForm
from app.auth import authentication as at
from app.catalog import main
from app.auth.models import User
from app import loginmanager



@at.route('/register',methods=['GET','POST'])
def register_user():
	
	if current_user.is_authenticated:
		flash('You are already Logged In')
		return redirect(url_for('main.book_details'))

	form = RegistrationForm()

	if form.validate_on_submit():    #POST request
		User.create_user(name=form.name.data,email=form.email.data,password=form.password.data)
		flash('Registration Successful')
		return redirect(url_for('authentication.do_the_login'))
	return render_template('registration.html',form = form)       #GET request

	
@at.route('/login',methods=['GET','POST'])
def do_the_login():

	if current_user.is_authenticated:
		flash('You are already Logged In')
		return redirect(url_for('main.book_details'))

	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by(user_email=form.email.data).first()
		if not user or not user.check_pasword(form.password.data):
			flash('Invalid credentails, Please try again later','error')
			return redirect(url_for('authentication.do_the_login'))

		login_user(user)
		flash('Logged in successfully')
		return redirect(url_for('main.book_details'))
	return render_template('login.html',form=form)

@at.route('/logout',methods=['GET','POST'])
@login_required
def do_the_logout():
	logout_user()
	flash('You are logged out')
	return redirect(url_for('main.book_details'))

@at.app_errorhandler(404)
def page_not_found(error):
	return render_template('404error.html'), 404

@loginmanager.user_loader    #stores user_id in session
def load_user(id):            # returns user object
	return User.query.get(int(id))

