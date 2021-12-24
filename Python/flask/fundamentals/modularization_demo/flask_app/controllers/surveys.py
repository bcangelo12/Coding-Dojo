from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import survey

@app.route('/')
def form_blank():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def form_filled():
    print("Got survey info")
    session['username'] = request.form['name']
    session['dojolocation'] = request.form['location']
    session['favlang'] = request.form['lang']
    session['usercomment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def return_form():
    return render_template('show.html')