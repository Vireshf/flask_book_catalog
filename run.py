from app import create_app,db
from app.auth.models import User

if __name__ == '__main__':
	flask_app = create_app('prod')
	with flask_app.app_context():
		db.create_all()
		if not User.query.filter_by(user_name='viru').first():
			User.create_user('viru','viru@gmail.com','12345')
			
	flask_app.run()