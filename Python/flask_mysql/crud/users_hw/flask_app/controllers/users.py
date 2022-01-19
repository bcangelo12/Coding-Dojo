from flask_app import app
from flask_bycrpt import Bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
bcrypt = Bcrypt(app)

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
    # print(request.form)
    # new_id = User.save(request.form)
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "username" : request.form['username'],
        "password" : pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect(f"/users/show/{new_id}") #new addition to load single user on creation

@app.route("/users/edit/<int:id>")
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit_user.html",user=User.get_one(data))

@app.route("/users/show/<int:id>")
def show(id):
    data = {
        "id":id
    }
    return render_template("one_user.html",user=User.get_one(data))

@app.route("/users/update", methods=["POST"])
def update():
    User.update(request.form)
    return redirect("/users")

@app.route("/users/destroy/<int:id>")
def destroy(id):
    data = {
        "id":id
    }
    User.destory(data)
    return redirect("/users")