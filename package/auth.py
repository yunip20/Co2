from venv import create
from flask import Blueprint, Flask, render_template, request, flash, redirect, session, url_for
from flask_login import login_user, login_required, logout_user, current_user, UserMixin 
from flask_mysqldb import MySQL
from pymysql import IntegrityError 
from werkzeug.security import generate_password_hash, check_password_hash 
from sqlalchemy.ext.automap import automap_base
from . import db 
 
auth = Blueprint('auth', __name__) 

@auth.route('/login', methods=['GET', 'POST'])
def login():  
    if request.method == 'POST' and 'email' in request.form and 'pw' in request.form:   
        user = request.form['email']
        pw = request.form['pw']  
        Base = automap_base(cls=(UserMixin, db.Model))
        Base.prepare(db.engine, reflect =True) 
        Calc_user = Base.classes.Calc_user
        # cursor = db.Table('Calc_user', db.metadata, autoload=True, autoload_with=db.engine)  
        results = db.session.query(Calc_user).filter(Calc_user.id == user).first()   
        if results is not None :    
            if check_password_hash(results.pw, pw):
                    login_user(results, remember=True)  
                    flash('Logged in successfully!', category='success') 
                    return redirect(url_for('views.home'))
            else:  
                flash('Incorrect password, try again.', category='error')  
        else:   
            flash('Email does not exist. Please sign up.', category ='error')
    
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST' and 'firstName' in request.form and 'pw2' in request.form and 'pw' in request.form and 'email' in request.form and 'lastName' in request.form: 
        user = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        pw = request.form.get('pw')
        pw2 = request.form.get('pw2') 
        Base = automap_base(cls=(UserMixin, db.Model))
        Base.prepare(db.engine, reflect =True) 
        Calc_user = Base.classes.Calc_user
        missing = db.session.query(Calc_user).filter(Calc_user.id == user).first() 
        if missing is not None:  
            flash('Email already exists', category='error')
        elif pw != pw2:
            flash('Passwords don\'t match.', category='error')
        elif len(pw) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif len(first_name) <2:
            flash('First Name must be greater than 1 character', category="error")
        elif len(last_name) <2:
            flash('Last must be greater than 1 charactera', category="error")
        else: 
            new_user = Calc_user(id=user, pw=generate_password_hash(pw), 
                         first_name = first_name,  last_name = last_name)
            db.session.add(new_user)
            try:
                db.session.commit()    
                login_user(new_user, remember=True) 
                flash('Account created!', category='success') 
                return redirect(url_for('views.home'))
            except IntegrityError:
                db.session.rollback()
                flash('Unexpected Error Occured', category = "error")  

    return render_template("sign_up.html", user=current_user)
