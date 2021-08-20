from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired, NumberRange

## USER MANAGEMENT

class LoginForm(FlaskForm):
    username = TextField    ('Username', id='username_login'   , validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login'        , validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
    username = TextField('Username'     , id='username_create' , validators=[DataRequired()])
    email    = TextField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
    password = PasswordField('Password' , id='pwd_create'      , validators=[DataRequired()])

## END USER MANAGEMENT

class AddDataForm(FlaskForm):
    dataComment = TextField('Comment', id='dataComment_create', validators=[DataRequired()])
    dataValue = TextField('Value', id='dataValue_create', validators=[DataRequired(), NumberRange(0,100)])
