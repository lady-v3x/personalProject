from flask_app.config.mysqlconnection import connectToMySQL

class Q18:
    def __init__(self, data):
        self.id = data['id']
        self.realDeal = data['realDeal']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q18;"
        results = connectToMySQL('personal').query_db(query)
        realDeal= []
        for x in results:
            realDeal.append( cls(x) )
        return realDeal