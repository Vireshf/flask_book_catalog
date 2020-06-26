from app import create_app,db
from app.auth.models import User
from sqlalchemy import exc

flask_app = create_app('dev')
with flask_app.app_context():
	db.create_all()
	if not User.query.filter_by(user_email='root@gmail.com').first():
		admin = User.create_user('admin','root@gmail.com','1234')
		db.session.add(admin)
		db.session.commit()
			
	flask_app.run()