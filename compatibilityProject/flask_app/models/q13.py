from flask_app.config.mysqlconnection import connectToMySQL

class Q13:
    def __init__(self, data):
        self.id = data['id']
        self.cuisine = data['cuisine']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q13;"
        results = connectToMySQL('personal').query_db(query)
        cuisine= []
        for x in results:
            cuisine.append( cls(x) )
        return cuisine