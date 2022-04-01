from flask_app.config.mysqlconnection import connectToMySQL

class Q17:
    def __init__(self, data):
        self.id = data['id']
        self.options = data['options']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q17;"
        results = connectToMySQL('personal').query_db(query)
        option= []
        for x in results:
            option.append( cls(x) )
        return option