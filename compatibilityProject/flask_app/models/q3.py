from flask_app.config.mysqlconnection import connectToMySQL

class Q3:
    def __init__(self, data):
        self.id = data['id']
        self.education = data['education']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q3;"
        results = connectToMySQL('personal').query_db(query)
        edu= []
        for x in results:
            edu.append( cls(x) )
        return edu