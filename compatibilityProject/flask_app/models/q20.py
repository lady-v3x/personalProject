from flask_app.config.mysqlconnection import connectToMySQL

class Q20:
    def __init__(self, data):
        self.id = data['id']
        self.openClosed = data['openClosed']
        
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM q20;"
        results = connectToMySQL('personal').query_db(query)
        openClosed= []
        for x in results:
            openClosed.append( cls(x) )
        return openClosed