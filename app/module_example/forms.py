from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired, NumberRange


class AddDataForm(FlaskForm):
    dataComment = TextField('Comment', id='dataComment_create', validators=[DataRequired()])
    dataValue = TextField('Value', id='dataValue_create', validators=[DataRequired(), NumberRange(0,100)])
