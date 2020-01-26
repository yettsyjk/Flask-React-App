import datetime
#import * means import everything from peewee
from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('birds2.sqlite')
# DATABASE = PostgresqlDatabase('birds')

class User(UserMixin, Model):
    username: CharField(unique = True)
    email = CharField(unique = True)
    password = CharField()
#making db accessible to class
    class Meta:
        database = DATABASE


class Bird(Model):
    name = CharField()
    breed = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    owner = ForeignKeyField(User, backref = 'birds')
    
#When Python creates a class object, special construction instructions can be provided. Since the database isn't part of the class itself, this class constructor 
##information is provided through the special Meta class
    class Meta:
        database = DATABASE
        
 #will open a connection to the database, 
 #set up our datatables, 
 # and then close the database connection.   
 #The safe=True argument is adding the IF NOT EXISTS clause to the 
 #SQL query it's creating so that the table will only be created if it doesn not already exist
 # 
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Bird], safe=True)
    print("Bird and User TABLES Created")
    DATABASE.close()