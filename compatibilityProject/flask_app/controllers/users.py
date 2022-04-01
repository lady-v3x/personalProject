import imp
from os import stat_result
from xml.etree.ElementTree import fromstring
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.q1 import Q1
from flask_app.models.q3 import Q3
from flask_app.models.q4 import Q4
from flask_app.models.q5 import Q5
from flask_app.models.q6 import Q6
from flask_app.models.q7 import Q7
from flask_app.models.q8 import Q8
from flask_app.models.q9 import Q9
from flask_app.models.q10 import Q10
from flask_app.models.q11 import Q11
from flask_app.models.q12 import Q12
from flask_app.models.q13 import Q13
from flask_app.models.q14 import Q14
from flask_app.models.q15 import Q15
from flask_app.models.q16 import Q16
from flask_app.models.q17 import Q17
from flask_app.models.q18 import Q18
from flask_app.models.q19 import Q19
from flask_app.models.q20 import Q20
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("questions.html", states = Q1.getStates(), edu = Q3.getAll(), comm = Q4.getAll(),animal = Q5.getAll(), color=Q6.getAll(), entertain=Q7.getAll(),music=Q8.getAll(), sport=Q9.getAll(), inOutdoor=Q10.getAll(), introExtrovert=Q11.getAll(), drink=Q12.getAll(), cuisine=Q13.getAll(), options=Q14.getAll(), doThink=Q15.getAll(),sponStruct=Q16.getAll(), option=Q17.getAll(), realDeal=Q18.getAll(), convo=Q19.getAll(), openClosed=Q20.getAll() )

@app.route('/register', methods=['POST'])
def register():
    data = {
        "fName": request.form['fName'],
        "lName": request.form['lName'],
        "email": request.form['email'],
        "pw": bcrypt.generate_password_hash(request.form['pw']),
        "DOB": request.form['DOB'],
        "username": request.form['username'],
        "q1": session['q1'],
        "q2": session['q2'],
        "q3": session['q3'],
        "q4": session['q4'],
        "q5": session['q5'],
        "q6": session['q6'],
        "q7": session['q7'],
        "q8": session['q8'],
        "q9": session['q9'],
        "q10": session['q10'],
        "q11": session['q11'],
        "q12": session['q12'],
        "q13": session['q13'],
        "q14": session['q14'],
        "q15": session['q15'],
        "q16": session['q16'],
        "q17": session['q17'],
        "q18": session['q18'],
        "q19": session['q19'],
        "q20": session['q20']
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect("/dashboard")

@app.route('/questions')
def questions():
    return render_template("questions.html")

@app.route('/registration')
def registration():
    return render_template("registration.html")

@app.route('/edit/<int:id>')
def edit(id):
    data= {
        "id":id
    }
    return render_template("editAnswers.html", user = User.get_one(data),states = Q1.getStates(), edu = Q3.getAll(), comm = Q4.getAll(),animal = Q5.getAll(), color=Q6.getAll(), entertain=Q7.getAll(),music=Q8.getAll(), sport=Q9.getAll(), inOutdoor=Q10.getAll(), introExtrovert=Q11.getAll(), drink=Q12.getAll(), cuisine=Q13.getAll(), options=Q14.getAll(), doThink=Q15.getAll(),sponStruct=Q16.getAll(), option=Q17.getAll(), realDeal=Q18.getAll(), convo=Q19.getAll(), openClosed=Q20.getAll())

@app.route('/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/dashboard')

@app.route('/answered', methods=['POST'])
def answered():
    session['q1'] = request.form['q1']
    session['q2'] = request.form['q2']
    session['q3'] = request.form['q3']
    session['q4'] = request.form['q4']
    session['q5'] = request.form['q5']
    session['q6'] = request.form['q6']
    session['q7'] = request.form['q7']
    session['q8'] = request.form['q8']
    session['q9'] = request.form['q9']
    session['q10'] = request.form['q10']
    session['q11'] = request.form['q11']
    session['q12'] = request.form['q12']
    session['q13'] = request.form['q13']
    session['q14'] = request.form['q14']
    session['q15'] = request.form['q15']
    session['q16'] = request.form['q16']
    session['q17'] = request.form['q17']
    session['q18'] = request.form['q18']
    session['q19'] = request.form['q19']
    session['q20'] = request.form['q20']
    
    return redirect("/registration")

@app.route('/loginPage')
def loginPage():
    return render_template("login.html")

@app.route('/login', methods=['post'])
def login():
    data = {
                "email": request.form['email'],
                "pw" : bcrypt.generate_password_hash(request.form['pw'])
            }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/loginPage')
    if not bcrypt.check_password_hash(user_in_db.pw, request.form['pw']):
        flash("Invalid Password.")
        return redirect('/loginPage')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template("dashboard.html", user = User.get_one(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')