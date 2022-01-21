from asyncio.windows_events import NULL
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session


class Recipe:
    db = "recipes_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under30 = data['under30']
        self.datemade = data['datemade']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes (name,description,instructions,under30,datemade,user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(under30)s,%(datemade)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,under30=%(under30)s,datemade=%(datemade)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Recipe name must be at least 3 characters long!","recipe")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description must be at least 3 characters long!","recipe")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Instructions must be at least 3 characters long!","recipe")
            is_valid = False
        if recipe['datemade'] < str(1):
            flash("A valid date must be entered!","recipe")
            is_valid = False
        return is_valid