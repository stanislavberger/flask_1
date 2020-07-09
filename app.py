from flask import Flask, url_for, render_template, request, redirect, abort, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)


@app.route('/')
def new():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
