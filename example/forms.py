from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



class SearchForm(FlaskForm):
    Key_word = StringField("Key_word", validators=[DataRequired()])
    submit = SubmitField("Post")



