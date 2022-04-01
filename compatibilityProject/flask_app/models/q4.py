from flask_app.config.mysqlconnection import connectToMySQL

class Q4:
    def __init__(self, data):
        self.id = data['id']
        self.communication = data['communication']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q4;"
        results = connectToMySQL('personal').query_db(query)
        comm = []
        for x in results:
            comm.append( cls(x) )
        return comm