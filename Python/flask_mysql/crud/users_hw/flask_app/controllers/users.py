from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def users():
    return render_template("read_all.html",users=User.get_all())

@app.route("/users/new")
def new():
    return render_template("new_user.html")

@app.route("/users/create", methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect("/users")