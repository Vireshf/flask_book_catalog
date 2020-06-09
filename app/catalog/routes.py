from app.catalog import main
from app.catalog.models import Book, Publication
from flask import render_template,request,redirect,url_for,flash
from app import db
from flask_login import login_required
from app.catalog.forms import EditForm

@main.route('/')
@main.route('/books')
def book_details():
	books = Book.query.all()
	publications=[]
	for book in books:
		publication = Publication.query.filter_by(id=book.pub_id).first()
		book.pub_name = publication.name
		publications.append(publication.name)
	return render_template('home.html',books = books,publications = publications)

@main.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):
	publisher = Publication.query.filter_by(id=publisher_id).first()
	publisher_books = Book.query.filter_by(pub_id=publisher_id).all()
	return render_template("publisher.html",publisher = publisher, publisher_books=publisher_books)

@main.route('/deletebook/<book_id>', methods=['GET','POST'])
@login_required
def delete_book(book_id):
	book = Book.query.get(book_id)
	if request.method == 'POST':
		db.session.delete(book)
		db.session.commit()
		flash('book deleted successfully')
		return redirect(url_for('main.book_details'))
	return render_template('delete.html',book=book)

@main.route('/editbook/<book_id>',methods=['GET','POST'])
@login_required
def edit_book(book_id):
	form = EditForm()
	if form.validate_on_submit(): 
		book = Book.query.get(book_id)
		book.title = form.title.data
		book.format = form.format.data
		book.num_pages = form.num_pages.data
		db.session.add(book)
		db.session.commit()
		flash('Deatils are edited successfully')
		return redirect(url_for('main.book_details'))
	return render_template('edit.html',form = form)

@main.route('/books/create',methods=['GET','POST'])
def create_book():
	return "hello world"