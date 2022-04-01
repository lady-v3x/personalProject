from flask_app.config.mysqlconnection import connectToMySQL

class Q19:
    def __init__(self, data):
        self.id = data['id']
        self.convo = data['convo']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q19;"
        results = connectToMySQL('personal').query_db(query)
        convo= []
        for x in results:
            convo.append( cls(x) )
        return convo