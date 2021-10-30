# STARTUP PACK

## Init

    python3 -m venv env
    pip install importlib flask flask-bootstrap flask_sqlalchemy==2.4.4 flask_wtf flask-login importlib blueprint sqlalchemy==1.3.23 email_validator

## How to run :
```
export FLASK_APP=run
export FLASK_ENV=development
flask run
```
## How to add a module

Add the following dirs/files like this (or copy the example_module) :
```
└── module-name/
    ├── templates/
    ├── __init__.py
    ├── forms.py
    ├── models.py
    └── routes.py
```

Edit the file `__init__.py` of the app to load the new module in the function `register_blueprints()` like this : 
```
    new_module = import_module('app.module-name.routes')
    app.register_blueprint(new_module.blueprint)
```

Modify the name of the blueprint in the `__init__.py` of the new module

Modify the imports in this 2 files :
```
└── module-name
    ├── models.py
    └── routes.py
```