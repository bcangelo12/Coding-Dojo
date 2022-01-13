from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import dojo, ninja

@app.route('/new')
def new_ninja():
    return render_template("new_ninja.html",dojos=dojo.Dojo.get_all())

@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    print(request.form)
    new_id = ninja.Ninja.save(request.form)
    return redirect("/")