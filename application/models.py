import flask
from application import db


class Users(db.document):
    user_id = db.ObjectIdField( unique=True )
    Name = db.StringField( max_length=50 )
    email = db.StringField( max_length=50 )
    Mobile = db.IntField( max_length=50 )
    Password = db.StringField( max_length=50 )


class Products(db.document):
    ProductID = db.ObjectIdField( unique=True )
    Name =  db.StringField( max_length=50 )
    Buying_rate = db.StringField( max_length=50 )
    Selling_rate = db.StringField( max_length=50 )

class Orders(db.document):

    OrderID = db.ObjectIdField( unique=True )
    user_id = db.IntField()
    ProductID = db.StringField()
    quality = db.IntField()
    Total=db.IntField()
