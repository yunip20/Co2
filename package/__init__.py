from sre_constants import SUCCESS
from flask import Flask 
from flask_mysqldb import MySQL
from flask_login import LoginManager, UserMixin
from sqlalchemy import create_engine     
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime  
from sqlalchemy.ext.automap import automap_base
 

db = SQLAlchemy()  

def create_app(): 
        app = Flask(__name__)   
        app.config['SECRET_KEY'] = 'super-secret' 
        app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:BTGxdbsdl123@localhost/CarbonEmission'  
        db.init_app(app) 
        login_manager = LoginManager()
        login_manager.init_app(app)
        with app.app_context():
            db.create_all()
        # app.config['MYSQL_HOST'] = db['mysql_host'] 
        # app.config['MYSQL_USER'] = db['mysql_user']
        # app.config['MYSQL_PASSWORD'] = db['mysql_password']
        # app.config['MYSQL_DB']= db['mysql_db']   
        from .auth import auth
        from .views import views 
        
        app.register_blueprint(auth, url_prefix= '/')
        app.register_blueprint(views, url_prefix= '/')  
        login_manager = LoginManager()
        login_manager.login_view = 'auth.login'
        login_manager.init_app(app)

        @login_manager.user_loader
        def load_user(id):    
               Base = automap_base(cls=(UserMixin, db.Model))
               Base.prepare(db.engine, reflect =True)
               Calc_user = Base.classes.Calc_user
               return Calc_user.query.get(id) 
        return app
    

 

 
 
 
