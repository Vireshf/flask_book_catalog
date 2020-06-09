from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField
from wtforms.validators import DataRequired, Email, Length,ValidationError,EqualTo

class EditForm(FlaskForm):

	title = StringField('Enter the book Title',validators=[DataRequired()])
	format = StringField('Enter the book Format',validators=[DataRequired()])
	num_pages = StringField('Enter the book Pages',validators=[DataRequired()])
	submit = SubmitField('Submit')