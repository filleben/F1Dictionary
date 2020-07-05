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
if path.exists("env.py"):
  import env 

#CSRF Setup
CSRF = CSRFProtect()

def create_app():
    CSRF.init_app(app)

#Environment Variable Setup
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config["MONGO_DBNAME"] = "f1_dictionary"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

#Login Form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

#Register Form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

#Home Page Route
@app.route('/')
@app.route('/display_definitions')
def display_definitions():
    """
    Displays all definitions from the definitions database in each category
    """
    a_f = mongo.db.definitions.find({"category_name": "A-F"})
    g_l = mongo.db.definitions.find({"category_name": "G-L"})
    m_r = mongo.db.definitions.find({"category_name": "M-R"})
    s_z = mongo.db.definitions.find({"category_name": "S-Z"})
    return render_template('index.html', A_F=a_f, G_L=g_l, M_R=m_r, S_Z=s_z)

#Add Definition Route
@app.route('/add_definition')
def add_definition():
    """
    Displays the add definition form
    """
    return render_template('addDefinition.html', categories=mongo.db.categories.find())

#Insert Definition Route
@app.route('/insert_definition', methods=['POST'])
def insert_definition():
    """
    Takes data from add definition form, inserts it into definitions database and redirects to home page
    """
    definitons = mongo.db.definitions
    definitons.insert_one(request.form.to_dict())
    return redirect(url_for('display_definitions'))

#Definition List Route
@app.route('/definition_list')
def definition_list():
    """
    Displays the definition list form
    """
    return render_template('definitionList.html', terms=mongo.db.definitions.find())

#Edit Definition Route
@app.route('/edit_definition/<term_id>')
def edit_definition(term_id):
    """
    Populates the edit definition form with data from the definitions database depending on which record it being edited
    """
    the_definition =  mongo.db.definitions.find_one({"_id": ObjectId(term_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editDefinition.html', term=the_definition, categories=all_categories)

#Update Definition Route
@app.route('/update_definition/<term_id>', methods=["POST"])
def update_definition(term_id):
    """
    Takes data from edit definition form, updates data in the definitions database for the term selected
    """
    definitions = mongo.db.definitions
    definitions.update( {'_id': ObjectId(term_id)},
    {
        'category_name':request.form.get('category_name'),
        'name': request.form.get('name'),
        'definition': request.form.get('definition'),
    })
    return redirect(url_for('definition_list'))

#Delete Term Route
@app.route('/delete_term/<term_id>')
def delete_term(term_id):
    """
    Deletes record from the definitions database
    """
    mongo.db.definitions.remove({'_id': ObjectId(term_id)})
    return redirect(url_for('definition_list'))

#Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Checks if a user is logged in already, 
    checks username and password against records in the user database
    """
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

#Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Checks if a user is logged in already, 
    checks if username matches any record in the users database, 
    inserts new user record into users database
    """
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

#Logout Route
@app.route('/logout')
def logout():
    """
    Logs users out of the site, redirects to home page
    """
    session.clear() 
    return redirect(url_for('display_definitions'))

#404 Errorhandler
@app.errorhandler(404)
def page_not_found(e):
    """
    Displays 404 page for any page not found errors
    """
    return render_template('404.html', title="Page Not Found!"), 404

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)