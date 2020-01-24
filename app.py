from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager
#Load and initialize all modules in app.py
#jsonify let\'s us send complex data types
#initialize an instancd of the Flask Class
#import global proxy from Flask


#This starts the website!
app = Flask(__name__)
app.secret_key = 'anysecretkey'
login_manager = LoginManager()
login_manager.init_app(app)

#import the models
import models

#look inside resources directory and look for file clouds and import clouds
from resources.users import users
from resources.clouds import clouds

#login
@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

@login_manager.unauthorized_handler
def unauthorized():
    return jsonify(
        data = {
            'error': 'User not logged in.'
        },
        status = {
            'code:': 401,
            'message: ': 'You must be logged in to access that resource.'
        }
    )

#CORS whitelist
CORS(users, origins = ['http://localhost:3000'], supports_credentials = True)
CORS(clouds, origins = ['http://localhost:3000'], supports_credentials = True)

#localhost:8000/api/v1/clouds
app.register_blueprint(users, url_prefix = '/api/v1/users')
app.register_blueprint(clouds, url_prefix = '/api/v1/clouds')


#set up the connection and close logic for requests
@app.before_request
def before_request():
    """Connnect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()
#always close the connection
@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

#default URL ending in "localhost:8000/recipes/"
@app.route('/')
def index():
    # my_list = ["let", "me", "start", "coding"]
    #the return determines what is displayed
    return 'hi'

# #CREATE NEW ROUTE
# @app.route('/json')
# def cloud():
#     return jsonsify(name="Cumulus", genus="Cumulus")

# #
# @app.route('/sayhi/<username>')
# def hello(username):
#     return "Hello {}".format(username)

#run the app when program starts
DEBUG = True
PORT = 8000
if __name__ == '__main__':
    #call initialize from models.py
    models.initialize()
    app.run(debug=DEBUG, port=PORT)