from flask_app.config.mysqlconnection import connectToMySQL

class Q6:
    def __init__(self, data):
        self.id = data['id']
        self.color = data['color']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q6;"
        results = connectToMySQL('personal').query_db(query)
        color= []
        for x in results:
            color.append( cls(x) )
        return color