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
    
if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)