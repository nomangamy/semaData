from flask import Flask

from  extensions import db 


class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    email = db.Column(db.String(100),unique =-True,nullable = False)
    first_name = db.Column(db.String(200),nullable=False,unique =False)
    second_name = db.Column(db.String(200),nullable=False,unique =False)
    password = db.Column(db.String(200),nullable =False,unique=False)

    def __repr__(self):
        return f"User('{self.user_id})'"

