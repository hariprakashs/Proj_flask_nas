import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "Iamkkl123"
    MONGODB_SETTINGS ={'db' : 'nutsandspices'} 
