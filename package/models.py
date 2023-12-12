from flask import session
from flask_login import UserMixin 
from sqlalchemy.ext.automap import automap_base 

# automap base
Base = automap_base()   

class Calc_user(Base, UserMixin):
    __tablename__ = 'Calc_user' 

class Info(Base, UserMixin):
    __tablename__ = 'Info' 