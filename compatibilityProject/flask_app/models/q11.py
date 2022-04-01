from flask_app.config.mysqlconnection import connectToMySQL

class Q11:
    def __init__(self, data):
        self.id = data['id']
        self.introExtrovert = data['introExtrovert']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q11;"
        results = connectToMySQL('personal').query_db(query)
        introExtrovert= []
        for x in results:
            introExtrovert.append( cls(x) )
        return introExtrovert