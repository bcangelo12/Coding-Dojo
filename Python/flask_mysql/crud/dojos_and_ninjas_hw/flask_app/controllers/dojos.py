from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect("/dojos")

@app.route('/dojos')
def dojos():
    return render_template("dojos.html",dojos=Dojo.get_all())

@app.route('/show/<int:id>')
def show_dojo(id):
    data = {
        "id":id
    }
    return render_template("show.html",dojo=Dojo.get_dojos_with_ninjas(data))

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect("/dojos")