from flask_app import app # NEED this line for app.route() among other things
from flask import render_template, redirect, request
from flask_app.models import team # Import your models here

# Controllers contan all the logic for all your routes.  They call on the models, which
# will handle all the interactions with the database.

# We will be using @app.route() here.

# Let's figure out the routes we'll need in these controllers - along with whether it's a GET or POST request:
# 1A. Show all teams
# 1B. Show one team - eventually with players later this week - to be added Wednesday
# 2A. Page with form to add a team
# 2B. Route to actually add to database
# 3A. Page to edit a team
# 3B. Route to edit in the database
# 4. Delete a team - to be added Wednesday

# we'll write out the logic in the lecture.

@app.route("/teams")
def show_all_teams():
    all_teams = team.Team.grab_all_teams()
    return render_template("all_teams.html", all_teams = all_teams)

@app.route("/teams/<int:id>")
def show_one_team(id):
    data = {
        "id":id
    }
    one_team = team.Team.grab_one_team(data)
    return render_template("show_team.html",this_team = one_team)

# Page to SHOW THE FORM where you will add a team
@app.route("/teams/new")
def show_add_team_form():
    return render_template("add_team.html")

# Route to add the team to the DATABASE
@app.route("/teams/add_to_database", methods=["POST"])
def add_team_to_db():
    data = {
        "city": request.form["city"],
        "nickname": request.form["nickname"],
        "stadium_name": request.form["stadium_name"],
    }
    team.Team.create_one(data)
    # print(request.form)
    return redirect("/teams")

# Route tp show the form where we'll edit an individual team
@app.route("/teams/<int:id>/edit_page")
def edit_team_form(id):
    data = {
        "id": id
    }
    this_team = team.Team.grab_one_team(data)
    return render_template("edit_team.html", this_team = this_team)

# Route to edit in the DATABASE
@app.route("/teams/<int:id>/edit", methods=["POST"])
def edit_team_in_db(id):
    data = {
        "id": id, # Need to pass in the team id to know which one we'll edit
        "city": request.form["city"],
        "nickname": request.form["nickname"],
        "stadium_name": request.form["stadium_name"],
    }
    team.Team.edit_one_team(data)
    return redirect("/teams")

@app.route("/teams/<int:id>/delete", methods=["POST"])
def delete_team(id):
    data = {
        "id":id
    }
    team.Team.delete_team(data)
    return redirect("/teams")