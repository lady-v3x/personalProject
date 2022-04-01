from flask_app.config.mysqlconnection import connectToMySQL

class Q9:
    def __init__(self, data):
        self.id = data['id']
        self.sport = data['sport']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q9;"
        results = connectToMySQL('personal').query_db(query)
        sport= []
        for x in results:
            sport.append( cls(x) )
        return sport