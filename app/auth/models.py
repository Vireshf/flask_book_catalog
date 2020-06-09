from app import db,bcrypt
from datetime import datetime
from app import loginmanager
from flask_login import UserMixin

class User(UserMixin,db.Model):

	__tablename__ = 'users'

	id = db.Column(db.Integer,primary_key = True)
	user_name =  db.Column(db.String(80),nullable = False)
	user_email = db.Column(db.String(80),nullable = False, unique = True, index = True)
	user_password = db.Column(db.String(80),nullable = False)
	registration_date = db.Column(db.DateTime,default = datetime.now)

	@classmethod
	def create_user(cls,name,email,password):
		user = cls(user_name = name, user_email=email, user_password=bcrypt.generate_password_hash(password).decode('utf-8'))

		db.session.add(user)
		db.session.commit()
		return user

	def check_pasword(self,password):
		return bcrypt.check_password_hash(self.user_password,password)

@loginmanager.user_loader    #stores user_id in session
def load_user(id):            # returns user object
	return User.query.get(int(id))