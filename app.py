from flask import Flask, jsonify, g
#jsonify let\'s us send complex data types
#initialize an instancd of the Flask Class
#import global proxy from Flask


#This starts the website!
app = Flask(__name__)

#import the models
import models
#set up the connection and close logic for requests
@app.before_request
def before_request():
    """Connnect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db = models.DATABASE
    g.db.connect()

@app.route('/json')
def cloud():
    return jsonsify(name="Cumulus", genus="Cumulus")

#default URL ending in "localhost:8000/recipes/"
@app.route('/')
def index():
    my_list = ["let", "me", "start", "coding"]
    #the return determines what is displayed
    return 'connected url'





#run the app when program starts
DEBUG = True
PORT = 8000
if __name__ == '__main__':
    #call initialize from models.py
    models.initialize()
    app.run(debug=DEBUG, port=PORT)