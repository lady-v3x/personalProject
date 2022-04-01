from flask_app.config.mysqlconnection import connectToMySQL

class Q10:
    def __init__(self, data):
        self.id = data['id']
        self.inOutdoor = data['inOutdoor']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q10;"
        results = connectToMySQL('personal').query_db(query)
        inOutdoor= []
        for x in results:
            inOutdoor.append( cls(x) )
        return inOutdoor