from flask_app.models.recipe import Recipe
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user, recipe

@app.route("/recipes/new")
def new_recipe():
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id" : session['user_id']
    }
    return render_template("new_recipe.html",users=user.User.get_by_id(data))

@app.route("/recipes/edit/<int:id>")
def edit_recipe(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id" : id
    }
    return render_template("edit_recipe.html",recipe=recipe.Recipe.get_one(data))

@app.route("/recipes/update", methods=['POST'])
def update_recipe():
    if "user_id" not in session:
        return redirect("/logout")
    if not recipe.Recipe.validate_recipe(request.form):
        id = request.form['id']
        return redirect(f"/recipes/edit/{id}")
    Recipe.update(request.form)
    return redirect("/dashboard")

@app.route("/recipes/<int:id>")
def show_recipe(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id" : id
    }
    return render_template("show_recipe.html",recipe=recipe.Recipe.get_one(data))

@app.route("/recipes/create", methods=['POST'])
def create_recipe():
    if "user_id" not in session:
        return redirect("/logout")
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect("/recipes/new")
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "datemade" : request.form['datemade'],
        "under30" : request.form['under30'],
        "user_id" : session['user_id']
    }
    id = recipe.Recipe.save(data)
    session['recipe_id'] = id
    return redirect("/dashboard")

@app.route("/recipes/destroy/<int:id>")
def destroy(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id" : id
    }
    Recipe.destroy(data)
    return redirect("/dashboard")