from flask_app.config.mysqlconnection import connectToMySQL

class Q5:
    def __init__(self, data):
        self.id = data['id']
        self.animal = data['animal']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q5;"
        results = connectToMySQL('personal').query_db(query)
        animal= []
        for x in results:
            animal.append( cls(x) )
        return animal