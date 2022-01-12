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