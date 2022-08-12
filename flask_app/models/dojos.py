from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.ubication = data['ubication']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save_survey(cls, survey):
        query = "INSERT INTO dojos (name, ubication, language, comment) VALUES (%(name)s, %(ubication)s, %(language)s, %(comment)s);"
        result = connectToMySQL('esquema_encuesta_dojo').query_db(query, survey)
        return result
    
    @classmethod
    def get_temporal_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        result = connectToMySQL('esquema_encuesta_dojo').query_db(query)
        user = cls(result[0])
        return user
    
    @staticmethod
    def validate_fields(survey):
        is_valid =  True
        if len(survey['name']) < 3:
            is_valid = False
            flash ('Name must be al least 3 characters.' , 'register')
        if len(survey['ubication']) <= 0:
            is_valid = False
            flash ('Please must choose a one location.' , 'register')
        if len(survey['language']) <= 0:
            is_valid = False
            flash ('Please must choose a one language.' , 'register')
        if len(survey['comment']) < 1:
            is_valid = False
            flash ("The comment can not be empty. Please write something." , 'register')
        return is_valid