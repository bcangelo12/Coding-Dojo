import re
from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session

class Pie:
    db = "pypie_derby_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.filling = data['filling']
        self.crust = data['crust']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pies;"
        results = connectToMySQL(cls.db).query_db(query)
        pies = []
        for pie in results:
            pies.append(cls(pie))
        return pies
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO pies (name,filling,crust,user_id) VALUES (%(name)s,%(filling)s,%(crust)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM pies WHERE id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query = "UPDATE pies SET name=%(name)s,filling=%(filling)s,crust=%(crust)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM pies WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
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
