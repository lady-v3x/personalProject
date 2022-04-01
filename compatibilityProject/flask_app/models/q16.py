from flask_app.config.mysqlconnection import connectToMySQL

class Q16:
    def __init__(self, data):
        self.id = data['id']
        self.sponStruct = data['sponStruct']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q16;"
        results = connectToMySQL('personal').query_db(query)
        sponStruct= []
        for x in results:
            sponStruct.append( cls(x) )
        return sponStruct