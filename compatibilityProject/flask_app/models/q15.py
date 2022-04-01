from flask_app.config.mysqlconnection import connectToMySQL

class Q15:
    def __init__(self, data):
        self.id = data['id']
        self.doThink = data['doThink']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q15;"
        results = connectToMySQL('personal').query_db(query)
        doThink= []
        for x in results:
            doThink.append( cls(x) )
        return doThink