
from flask import render_template, Flask, request
from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)
import logging

from app import db, login_manager
from app.base import blueprint
from app.base.models import User
from app.base.forms import LoginForm, CreateAccountForm
from app.base.util import verify_pass


@blueprint.route('/')
def route_default():
    return render_template( 'index.html')
    #return '<p>Welcome</p>'

# Login

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if ('login' in request.form):
        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = User.query.filter_by(username=username).first()
        
        # Check the password
        if user and verify_pass( password, user.password):
            login_user(user)
            logging.info('User connected : ' + username)
            return redirect(url_for('base_blueprint.route_default'))

        # Something (user or pass) is not ok
        return render_template( 'login/login.html', form=login_form, msg='Login failed')

    if not current_user.is_authenticated:
        return render_template( 'login/login.html', form=login_form)
    return redirect(url_for('base_blueprint.route_default'))

@blueprint.route('/register', methods=['GET', 'POST'])
def user_management():
    register_form = CreateAccountForm(request.form)
    
    if ('register' in request.form):
        username = request.form['username']
        email = request.form['email']

        user = User.query.filter_by(username=username).first()
        if (user):
            # Username already created
            return render_template( 'login/register.html', 
                                    msg='Username already registered', 
                                    success=False,
                                    form=register_form)
        
        user = User.query.filter_by(email=email).first()
        if (user):
            # email already created
            return render_template( 'login/register.html', 
                                    msg='Email already registered', 
                                    success=False,
                                    form=register_form)

        # Otherwise, create user
        user = User(username=username, email=email, password=request.form['password'])
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('base_blueprint.login'))
    else: 
        return render_template('login/register.html', form=register_form)

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('base_blueprint.login'))

# END LOGIN BLOCK


## ERRORS

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('errors/403.html'), 403

## END ERRORS



