# Controller will be built Wednesday

from flask_app import app # NEED this line for app.route() among other things
from flask import render_template, redirect, request
from flask_app.models import player # Import your models here

# Controllers contan all the logic for all your routes.  They call on the models, which
# will handle all the interactions with the database.

# We will be using @app.route() here.

# Let's figure out the routes we'll need in these controllers - along with whether it's a GET or POST request:
# 1A. Show all players
# 1B. Show one player - with a team
# 2A. Page with form to add a player
# 2B. Route to actually add to database
# 3A. Page to edit a player
# 3B. Route to edit in the database
# 4. Delete a player

# we'll write out the logic in the lecture.

@app.route("/players")
def show_all_players():
    all_players = player.Player.grab_all_players_without_teams() # We'll link teams in the lecture!
    return render_template("all_players.html", all_players = all_players)

# Page to SHOW THE FORM where you will add a player
@app.route("/players/new")
def show_add_player_form():
    return render_template("add_player.html")

# Route to add the player to the DATABASE
@app.route("/players/add_to_database", methods=["POST"])
def add_player_to_db():
    data = {
        "city": request.form["city"],
        "nickname": request.form["nickname"],
        "stadium_name": request.form["stadium_name"],
    }
    player.Player.create_one(data)
    # print(request.form)
    return redirect("/players")

# Route tp show the form where we'll edit an individual player
@app.route("/players/<int:id>/edit_page")
def edit_player_form(id):
    data = {
        "id": id
    }
    this_player = player.Player.grab_one_player_without_team(data) # This WILL change so the team IS added
    return render_template("edit_player.html", this_player = this_player)

# Route to edit in the DATABASE
@app.route("/players/<int:id>/edit", methods=["POST"])
def edit_player_in_db(id):
    data = {
        "id": id, # Need to pass in the player id to know which one we'll edit
        "first_name": request.form["first_name"], 
        "last_name": request.form["last_name"], 
        "number": request.form["number"],
        "position": request.form["position"], 
        "team_id": request.form["team_id"],
    }
    player.Player.edit_one_player(data)
    return redirect("/players")