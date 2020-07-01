import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "f1_dictionary"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

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
    
if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)