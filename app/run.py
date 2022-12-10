from flask import Flask,request,render_template
from flask import Flask, abort
from flask import jsonify   
from flask_admin.contrib.sqla import ModelView
from flask import session, redirect, url_for, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

import pickle

app = Flask(__name__)
@app.errorhandler(404) 
def invalid_route(e): 
    return jsonify({'Þetta er 404 error page'})
@app.errorhandler(500) 
def invalid_route(e): 
    return jsonify({'Þetta er 404 error page'})


@app.route('/')
def hello_world():
    return render_template("login.html")
database={'admin':'admin','admin':'admin','admin':'admin'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html',info="Invalid User")
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid password')
        else:
                return render_template('home.html',name=name1)





@app.route("/dashboard")
def dashboard():    
    return render_template("dashboard.html")

@app.route("/Text")
def text():
    return render_template("text.html")

            
    

if __name__ == '__main__':
    app.run()