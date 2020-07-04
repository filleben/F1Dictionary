import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, TextAreaField, IntegerField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Optional
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if os.path.exists("env.py"):
  import env 

CSRF = CSRFProtect()

def create_app():
    CSRF.init_app(app)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config["MONGO_DBNAME"] = "f1_dictionary"
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

@app.route('/')
@app.route('/display_definitions')
def display_definitions():
    a_f = mongo.db.definitions.find({"category_name": "A-F"})
    g_l = mongo.db.definitions.find({"category_name": "G-L"})
    m_r = mongo.db.definitions.find({"category_name": "M-R"})
    s_z = mongo.db.definitions.find({"category_name": "S-Z"})
    return render_template('index.html', A_F=a_f, G_L=g_l, M_R=m_r, S_Z=s_z)

@app.route('/add_definition')
def add_definition():
    return render_template('addDefinition.html', categories=mongo.db.categories.find())

@app.route('/insert_definition', methods=['POST'])
def insert_definition():
    definitons = mongo.db.definitions
    definitons.insert_one(request.form.to_dict())
    return redirect(url_for('display_definitions'))

@app.route('/definition_list')
def definition_list():
    return render_template('definitionList.html', terms=mongo.db.definitions.find())

@app.route('/edit_definition/<term_id>')
def edit_definition(term_id):
    the_definition =  mongo.db.definitions.find_one({"_id": ObjectId(term_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editDefinition.html', term=the_definition, categories=all_categories)

@app.route('/update_definition/<term_id>', methods=["POST"])
def update_definition(term_id):
    definitions = mongo.db.definitions
    definitions.update( {'_id': ObjectId(term_id)},
    {
        'category_name':request.form.get('category_name'),
        'name': request.form.get('name'),
        'definition': request.form.get('definition'),
    })
    return redirect(url_for('definition_list'))

@app.route('/delete_term/<term_id>')
def delete_term(term_id):
    mongo.db.definitions.remove({'_id': ObjectId(term_id)})
    return redirect(url_for('definition_list'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('display_definitions'))

    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.users
        logged_in_user = user.find_one({'name': request.form['username'].title()})

        if logged_in_user:
            if check_password_hash(logged_in_user['pass'], request.form['password']): 
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('display_definitions'))

            flash('Invalid credentials')
            return redirect(url_for('login'))
    return render_template('login.html', form=form, title='Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'logged_in' in session:
        return redirect(url_for('display_definitions'))

    form = RegistrationForm()
    if form.validate_on_submit():

        user = mongo.db.users
        duplicate_user = user.find_one({'name': request.form['username'].title()})

        if duplicate_user is None:
            hash_pass = generate_password_hash(request.form['password'])
            user.insert_one({'name': request.form['username'].title(), 'pass': hash_pass})
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('display_definitions'))

        flash('This username is already taken. Please try another.')
        return redirect(url_for('register'))
    return render_template('register.html', form=form, title="Register")

@app.route('/logout')
def logout():
    session.clear() 
    return redirect(url_for('display_definitions'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)