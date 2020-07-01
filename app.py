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
def display_definitions():
    a_f = mongo.db.definitions.find({"category_name": "A-F"})
    g_l = mongo.db.definitions.find({"category_name": "G-L"})
    m_r = mongo.db.definitions.find({"category_name": "M-R"})
    s_z = mongo.db.definitions.find({"category_name": "S-Z"})
    return render_template('base.html', A_F=a_f, G_L=g_l, M_R=m_r, S_Z=s_z)
    
if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)