import datetime
#import * means import everything from peewee
from peewee import *
from flask_login import UserMixin
# DATABASE = SqliteDatabase('clouds.sqlite')
DATABASE = PostgresqlDatabase('cloudApp')

class User(UserMixin, Model):
    username: CharField(unique = True)
    email = CharField(unique = True)
    password = CharField()
#making db accessible to class
    class Meta:
        database = DATABASE


class Cloud(Model):
    name = ForeignKeyField(User, backref = 'clouds')
    genus = CharField()
    form_level = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    
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
    DATABASE.create_tables([User, Cloud], safe=True)
    print("Cloud TABLES Created")
    DATABASE.close()