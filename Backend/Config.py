import os 

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config): 
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenvZ('DEV_DATABASE_URI') 
    

class Production(Config):
    DEBUG = False

class Testing(Config): 
    TESTING = True
