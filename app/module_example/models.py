from app.module_example import blueprint
from app import db, login_manager
from sqlalchemy import Binary, Column, Integer, String


class Data(db.Model):

    __tablename__ = 'Data'

    id = Column(Integer, primary_key=True)
    dataComment = Column(String)
    dataValue = Column(Integer)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]
                
            setattr(self, property, value)

    def __repr__(self):
        return str(self.dataComment + ' : ' + str(self.dataValue) )

