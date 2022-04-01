from flask_app.config.mysqlconnection import connectToMySQL

class Q12:
    def __init__(self, data):
        self.id = data['id']
        self.drink = data['drink']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q12;"
        results = connectToMySQL('personal').query_db(query)
        drink= []
        for x in results:
            drink.append( cls(x) )
        return drink