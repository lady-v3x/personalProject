from flask_app.config.mysqlconnection import connectToMySQL

class Q14:
    def __init__(self, data):
        self.id = data['id']
        self.options = data['options']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q14;"
        results = connectToMySQL('personal').query_db(query)
        options= []
        for x in results:
            options.append( cls(x) )
        return options