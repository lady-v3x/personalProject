from flask_app.config.mysqlconnection import connectToMySQL

class Q1:
    def __init__(self, data):
        self.id = data['id']
        self.state = data['state']
        
    @classmethod
    def getStates(cls):
        query = "SELECT * FROM q1;"
        results = connectToMySQL('personal').query_db(query)
        states = []
        for x in results:
            states.append( cls(x) )
        return states