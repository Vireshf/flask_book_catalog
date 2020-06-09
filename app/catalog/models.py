from app import db

import datetime


class Publication(db.Model):
	__tablename__ = 'publication'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80),nullable = False)

	def __init__(self,name):
		self.name = name

	def __repr__(self):
		return 'id is {} and name is {}'.format(self.id,self.name)

class Book(db.Model):
	__tablename__ = 'book'

	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(80),nullable = False, index = True)
	author = db.Column(db.String(80))
	avg_rating = db.Column(db.Float)
	format = db.Column(db.String(80))
	image = db.Column(db.String(80),unique = True)
	num_pages = db.Column(db.Integer)
	pub_date = db.Column(db.DateTime,default=datetime.datetime.utcnow())

	#foreign key
	pub_id = db.Column(db.Integer,db.ForeignKey('publication.id'))


	def __init__(self,title,author,avg_rating,format,image,num_pages,pub_id):
		self.title = title
		self.author = author
		self.avg_rating = avg_rating
		self.format = format
		self.image = image
		self.num_pages = num_pages
		self.pub_id = pub_id

	def __repr__(self):
		return 'title: {} and author : {}'.format(self.title,self.author)