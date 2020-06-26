from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField
from wtforms.validators import DataRequired, Email, Length,ValidationError,EqualTo

class EditForm(FlaskForm):

	title = StringField('Enter the book Title',validators=[DataRequired()])
	format = StringField('Enter the book Format',validators=[DataRequired()])
	num_pages = StringField('Enter the book Pages',validators=[DataRequired()])
	submit = SubmitField('Submit')

class BookForm(FlaskForm):

	title = StringField('Enter the Title',validators=[DataRequired(),Length(5,message="title should be of minimum length 3")])
	author = StringField('Enter the Author',validators=[DataRequired(),Length(5,message="Author should be of minimum length 3")])
	avg_rating = StringField('Enter the Average rating',validators=[DataRequired()])
	format = StringField('Enter the Format',validators=[DataRequired()])
	image = StringField('Enter the Image path',validators=[DataRequired()])
	num_pages = StringField('Enter the Number of pages',validators=[DataRequired()])
	publication = StringField('Enter the publication id',validators=[DataRequired()])
	submit = SubmitField('Submit')