# Will be built more Wednesday

from flask_app.config.mysqlconnection import connectToMySQL
# Might import other model files this week - stay tuned!

class Player:
    db_name = 'football_schema' # Make use of class variable to hold schema name
    
    # Model for the player - notice the names of the fields match those in the DB
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.number = data['number']
        self.position = data['position']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # DON'T NEED team_id - WE'LL LINK THE TEAM IN A DIFFERENT WAY!
        # Add field that holds the team itself as an object

    # We'll need to know how to:
    # CREATE (add) a player - done already
    # UPDATE (edit) a player - done already
    # DELETE a team - to be added Wednesday
    # READ data:
    # - One team without players
    # - One team with ALL players (later this week)
    # - All teams without players - done already
    # - Challenge on your own: ALL teams WITH players
    # - Later this week: start with players and...
    #     - Grab one player without team info - done already
    #     - Grab one player with team info
    #     - Grab ALL players with their teams

    # Method to create a new player - notice all the class methods!
    @classmethod
    def create_one(cls, data):
        # This is a prepared statement - notice the %() formats.
        # Use %()s, even for numers - MySQL will convert for you when saved in the database.
        query = "INSERT INTO players (first_name, last_name, number, position, team_id) VALUES (%(first_name)s, %(last_name)s, %(number)s, %(position)s, %(team_id)s);" # Add query here - test them in MySQL workbench!
        # Need the name of the schema in the connectToMySQL statemet
        return connectToMySQL(cls.db_name).query_db(query, data) # Returns an integer

    @classmethod
    def grab_one_player_without_team(cls, data):
        query = "SELECT * FROM players WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data) # Returns a list of dictionaries
        if len(results) > 0:
            return cls(results[0])
        else:
            return None

    @classmethod
    def edit_one_player(cls,data):
        query = "UPDATE players SET first_name = %(first_name)s, last_name = %(last_name)s, number = %(number)s, position = %(position)s, team_id = %(team_id)s, WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def grab_all_players_without_teams(cls):
        query = "SELECT * FROM players;"
        results = connectToMySQL(cls.db_name).query_db(query) # Returns a list of dictionaries
        # print(results)
        all_players = [] # List of Teams
        for this_player in results:
            player_class_instance = cls(this_player)
            all_players.append(player_class_instance)
        return all_players