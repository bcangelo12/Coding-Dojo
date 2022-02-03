from flask_app.models.pie import Pie
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import pie, user

@app.route("/pies")
def show_all_pies():
    if "user_id" not in session:
        return redirect("/logout")
    return render_template("pie_derby.html",pies=pie.Pie.get_all())

@app.route("/create/pie", methods=['POST'])
def new_pie():
    if "user_id" not in session:
        return redirect("/logout")
    if not pie.Pie.validate_pies(request.form):
        return redirect("/dashboard")
    data = {
        "name" : request.form['name'],
        "filling" : request.form['filling'],
        "crust" : request.form['crust'],
        "user_id" : session['user_id']
    }
    id = pie.Pie.save(data)
    session['pie_id'] = id
    return redirect("/dashboard")

@app.route("/pies/edit/<int:id>")
def edit_pie(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id" : id
    }
    return render_template("edit_pie.html",pie=pie.Pie.get_one(data))

@app.route("/pies/update", methods=['POST'])
def update_pie():
    if "user_id" not in session:
        return redirect("/logout")
    if not pie.Pie.validate_pies(request.form):
        id = request.form['id']
        return redirect(f"/pies/edit/{id}")
    Pie.update(request.form)
    return redirect("/dashboard")

@app.route("/show/<int:id>")
def show_pie(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id" : id
    }
    return render_template("show_pie.html",pie=pie.Pie.get_one(data),user=user.User.get_users_with_pies(data))

@app.route("/pies/destroy/<int:id>")
def destroy(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id" : id
    }
    Pie.destroy(data)
    return redirect("/dashboard")

@app.route("/add/one")
def add_one(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id" : id
    }
    Pie.add_like(data)
    return redirect("/pies")