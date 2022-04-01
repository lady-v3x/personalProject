from flask_app.config.mysqlconnection import connectToMySQL

class Q7:
    def __init__(self, data):
        self.id = data['id']
        self.entertainment = data['entertainment']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q7;"
        results = connectToMySQL('personal').query_db(query)
        entertain= []
        for x in results:
            entertain.append( cls(x) )
        return entertain