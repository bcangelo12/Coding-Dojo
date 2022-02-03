from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_app.models import pie

class User:
    db = "pypie_derby_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.pies = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
        
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_users_with_pies(cls,data):
        query = "SELECT * FROM users LEFT JOIN pies ON users.id = pies.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        user = cls(results[0])
        for row in results:
            recipe_data = {
                "id" : row['pies.id'],
                "name" : row['name'],
                "filling" : row['filling'],
                "crust" : row['crust'],
                "likes" : row['likes'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            user.pies.append(pie.Pie(recipe_data))
        return user

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.","register")
        if len(user['first_name']) < 2:
            flash("First name must be 2 or more characters and must be only letters!","register")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be 2 or more characters and must be only letters!","register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!","register")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password too weak! Must be at least 8 characters.","register")
            is_valid = False
        if user['password'] != user['confirm']:
            flash("Passwords must match!","register")
            is_valid = False
        return is_valid
