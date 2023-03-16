from flask import Flask, render_template, make_response, flash, redirect, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    response = make_response(render_template('login.html'))
    return response

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)