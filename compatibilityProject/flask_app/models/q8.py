from flask_app.config.mysqlconnection import connectToMySQL

class Q8:
    def __init__(self, data):
        self.id = data['id']
        self.music = data['music']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q8;"
        results = connectToMySQL('personal').query_db(query)
        music= []
        for x in results:
            music.append( cls(x) )
        return music