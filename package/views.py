from flask import Blueprint, redirect, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user, login_user, UserMixin   
from sqlalchemy.ext.automap import automap_base
from . import db 
 

views = Blueprint('views', __name__) 

@views.route('/', methods=['GET', 'POST'])
@login_required
def home(): 
    return render_template("home.html", user=current_user)


@views.route('/forms', methods=['GET', 'POST'])
@login_required
def forms(): 
    if request.method == 'POST' and 'date' in request.form and 'household' in request.form and 'address' in request.form:   
        report_date = request.form['date'] 
        num_household = request.form['household'] 
        zipcode = request.form['address'] 
        Base = automap_base(cls=(UserMixin, db.Model))
        Base.prepare(db.engine, reflect =True) 
        Calc_user = Base.classes.Calc_user
        # cursor = db.Table('Calc_user', db.metadata, autoload=True, autoload_with=db.engine)  
        results = db.session.query(Calc_user).filter(Calc_user.id ==  current_user).first()   
        if results is not None :     
            # result = db.engine.execute( )
            flash('Saved Successfully', category ='error')   
        else:   
            flash('Email does not exist. Please sign up.', category ='error')
     
    return render_template("forms.html", user=current_user)
 