import re
from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import user

class Pie:
    db = "pypie_derby_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.filling = data['filling']
        self.crust = data['crust']
        self.likes = data['likes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pies JOIN users ON pies.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        pies = []
        for pie in results:
            pie_class = cls(pie)
            user_dict = {
            "id": pie['users.id'],
            "first_name": pie['first_name'],
            "last_name": pie['last_name'],
            "email": pie['email'],
            "password": pie['password'],
            "created_at": pie['users.created_at'],
            "updated_at": pie['users.updated_at']
            }
            user_class = user.User(user_dict)
            pie_class.user = user_class
            pies.append(pie_class)
        return pies
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO pies (name,filling,crust,likes,user_id) VALUES (%(name)s,%(filling)s,%(crust)s,0,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM pies JOIN users ON pies.user_id = users.id WHERE pies.id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query = "UPDATE pies SET name=%(name)s,filling=%(filling)s,crust=%(crust)s, WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM pies WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def add_like(cls,data):
        query1 = "SELECT likes FROM pies WHERE id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query1,data)
        current_likes = cls(results[0])
        plus_one = current_likes + 1
        query2 =  "UPDATE pies SET likes = " + plus_one + "WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query2,data)

    @staticmethod
    def validate_pies(pie):
        is_valid = True
        if len(pie['name']) < 3:
            flash("Pie name must be at least 3 characters long!","pies")
            is_valid = False
        if len(pie['filling']) < 1:
            flash("Filling must be filled in!","pies")
            is_valid = False
        if len(pie['crust']) < 1:
            flash("Crust must be filled in!","pies")
            is_valid = False
        return is_valid

    @classmethod
    def get_pies_with_users(cls,data):
        query = "SELECT * FROM pies JOIN users ON pies.user_id = users.id;"
        return connectToMySQL(cls.db).query_db(query,data)
