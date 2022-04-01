from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.fName = data['fName']
        self.lName = data['lName']
        self.username = data['username']
        self.email = data['email']
        self.pw = data['pw']        
        self.DOB = data['DOB']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.q1 = data['q1_id']
        self.q2 = data['q2']
        self.q3 = data['q3_id']
        self.q4 = data['q4_id']
        self.q5 = data['q5_id']
        self.q6 = data['q6_id']
        self.q7 = data['q7_id']
        self.q8 = data['q8_id']
        self.q9 = data['q9_id']
        self.q10 = data['q10_id']
        self.q11 = data['q11_id']
        self.q12 = data['q12_id']
        self.q13 = data['q13_id']
        self.q14 = data['q14_id']
        self.q15 = data['q15_id']
        self.q16 = data['q16_id']
        self.q17 = data['q17_id']
        self.q18 = data['q18_id']
        self.q19 = data['q19_id']
        self.q20 = data['q20_id']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('personal').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (fName,lName,email,pw, DOB, username, createdAt, updatedAt, q1_id, q2, q3_id, q4_id, q5_id, q6_id, q7_id, q8_id, q9_id, q10_id, q11_id, q12_id, q13_id, q14_id, q15_id, q16_id, q17_id, q18_id, q19_id, q20_id) VALUES (%(fName)s,%(lName)s,%(email)s, %(pw)s, %(DOB)s, %(username)s, NOW(), NOW(), %(q1)s, %(q2)s, %(q3)s, %(q4)s, %(q5)s, %(q6)s, %(q7)s, %(q8)s, %(q9)s, %(q10)s,%(q11)s, %(q12)s, %(q13)s, %(q14)s, %(q15)s, %(q16)s, %(q17)s, %(q18)s, %(q19)s, %(q20)s);"
        result = connectToMySQL('personal').query_db(query, data)
        return result
    
    @classmethod
    def get_by_email(cls, data):
        query="SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('personal').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
        
    @classmethod
    def get_one(cls, data):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('personal').query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET q1_id=%(q1)s,q2=%(q2)s,q3_id=%(q3)s, q4_id=%(q4)s, q5_id=%(q5)s,q6_id=%(q6)s,q7_id=%(q7)s,q8_id=%(q8)s, q9_id=%(q9)s, q10_id=%(q10)s,q11_id=%(q11)s,q12_id=%(q12)s,q13_id=%(q13)s, q14_id=%(q14)s, q15_id=%(q15)s,q16_id=%(q16)s,q17_id=%(q17)s,q18_id=%(q18)s, q19_id=%(q19)s, q20_id=%(q20)s,updatedAt=NOW() WHERE id = %(id)s;"
        return connectToMySQL('personal').query_db(query, data)
        
    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('personal').query_db(query,data)

    @staticmethod
    def is_valid(user):
        is_valid = True
        query="SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('personal').query_db(query,user)
        if len(user['fName']) < 2:
            is_valid = False
            flash("First name must be at least 2 characters.")
        if len(user['lName']) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters.")
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email.")
            is_valid=False    
        if len(user['pw']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters long.")
        if user['pwConfirm'] != user['pw']:
            is_valid = False
            flash("Passwords do not match.")
        return is_valid