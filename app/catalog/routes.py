from app.catalog import main
from app.catalog.models import Book, Publication
from flask import render_template,request,redirect,url_for,flash
from app import db
from flask_login import login_required
from app.catalog.forms import EditForm,BookForm

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

@main.route('/admin/menu/options/deletebook/<book_id>', methods=['GET','POST'])
@login_required
def delete_book(book_id):
	book = Book.query.get(book_id)
	if request.method == 'POST':
		db.session.delete(book)
		db.session.commit()
		flash('book deleted successfully')
		return redirect(url_for('main.book_details'))
	return render_template('delete.html',book=book)

@main.route('/admin/menu/options/', methods=['GET','POST'])
@login_required
def delete_book_selected():
	books = Book.query.all()
	return render_template('delete_books.html',books=books)

@main.route('/admin/menu/options/editbook/<book_id>',methods=['GET','POST'])
@login_required
def edit_book(book_id):
	form = EditForm()
	book = Book.query.get(book_id)
	form.title.data = book.title
	form.format.data = book.format
	form.num_pages.data = book.num_pages
	if form.validate_on_submit():
		form = EditForm()
		book = Book.query.get(book_id)
		book.title = form.title.data
		book.format = form.format.data
		book.num_pages = form.num_pages.data
		db.session.add(book)
		db.session.commit()
		flash('Book details has been successfully updated')
		return redirect(url_for('main.book_details'))
	return render_template('edit.html',form = form)

@main.route('/admin/menu',methods=['GET','POST'])
def book_modify():
	return render_template('menu.html')

@main.route('/admin/menu/addbook',methods=['GET','POST'])
def add_new_book():
	form = BookForm()

	if form.validate_on_submit():
		book = Book(form.title.data,form.author.data,form.avg_rating.data,form.format.data,form.image.data,form.num_pages.data,form.publication.data)
		db.session.add(book)
		db.session.commit()
		flash('Book added successfully')
		return redirect(url_for('main.book_details'))

	return render_template('add_book.html',form = form)
