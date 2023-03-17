from flask import Flask, render_template, make_response, redirect, request, session, jsonify, url_for
from database import Database, AccountNotFound, PasswordIncorrect
from auth import Account
import os

app = Flask(__name__)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect('login')
    else:
        response = make_response(render_template('index.html'))
        return response

@app.route('/login')
def login():
    response = make_response(render_template('login.html'))
    return response

@app.route('/register')
def register():
    response = make_response(render_template('register.html'))
    return response

@app.route('/reg', methods=['POST'])
def registerAccount():
    account = Account(request.form['email'], request.form['password'], request.form['username'], "")
    try:
        db.addUser(account)
    except Exception as e:
        return str(e)
    
    return redirect('/login')

@app.route('/auth', methods=['POST'])
def authenticate():
    account = Account(request.json['email'], request.json['password'])
    try:
        db.login(account)
    except Exception as e:
        return jsonify({'error': str(e)})

    session['logged_in'] = True
    return jsonify({'redirect': '/'})

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

if __name__ == "__main__":
    db = Database()
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=80)