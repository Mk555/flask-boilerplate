from app.module_example import blueprint

from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager, db

from app.module_example.forms import AddDataForm
from app.module_example.models import Data


@blueprint.route('/form', methods=['GET', 'POST'])
@login_required
def addData():
    # Form to send to the template
    add_data_form = AddDataForm()

    if(request.method == 'GET'):
        template = 'pages/form.html'
    elif(request.method == 'POST'):
        template = 'pages/table_data.html'
        if ('addData' in request.form):
            value = request.form['dataValue']
            comment = request.form['dataComment']

            data = Data(**request.form)
            db.session.add(data)
            db.session.commit()
        return render_template('pages/table_data.html', data=Data.query.all())

    return render_template(template, form=add_data_form)

@blueprint.route('/data')
@login_required
def show_data():
    
    return render_template('pages/table_data.html', data=Data.query.all())