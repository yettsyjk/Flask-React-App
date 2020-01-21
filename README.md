# Flask-React-App
Flask React App course
Set up a Flask app. 
Flask-React-App at: https://github.com/yettsyjk/Flask-React-App.git
REACT-App Repo: https://github.com/yettsyjk/React-App-Repo.git

###Requirements
1. Create a repo that will be your flask app. Paste that repo above. Make sure to make it public. Fork and clone your repo in your homework directory.
1. Navigate inside and start the virtual environment: virtualenv .env -p python3
1. Now activate the environment: source .env/bin/activate
1. Confirm that (.env) is prepended to your command line. You must install everything and run your app inside this environment.
1. Install all your dependencies: pip3 install flask-bcrypt peewee flask psycopg2 flask_login flask_cors
1. (If you have issues with psycopg2, run: pip3 install psycopg2-binary)
1. Save your dependencies: pip3 freeze > requirements.txt
1. Set up a model with at least three properties. (We will be setting up a User model, so choose one where a user relationship makes sense.)
1. Use your models file to create a SQLite database.
1. Set up your app.
1. Set up your resource.
1. Set up Create, Index, Show, Update, and Delete routes for your resource.
1. Test with Postman.

###Setup
Let's also build a virtual environment. Virtual environments allow us to have multiple versions of Python on the same system so we can have different versions of both Python and the packages we are using on our computers.


#Run the following commands:
virtualenv .env -p python3
source .env/bin/activate
(If virtualenv isn't recognized, you may need to run pip3 install virtualenv.)

Notice that (.env) is now prepended to your command line. Make sure that you see that when you're working on your Flask app.

####Dependencies
Now let's set up our dependencies by running the following commands (if you get an error regarding psycopg2, try running pip3 install psycopg2-binary instead):
pip3 install flask-bcrypt peewee flask psycopg2 flask_login flask_cors
pip3 freeze > requirements.txt
We'll run the Flask app like any other app.

This process is similar to what we did with our Express apps, but we just do the process backwards. Instead of first creating the file that keeps track of our dependences (like package.json did in Express), we install our app and dependences(the pip3 install command). Then, we save all our dependencies to a text file that will keep track of them (the pip3 freeze command) within our virtualenv.

This means that, in the same way that we could clone a project and just run npm i or npm install because all the dependencies were listed in package.json, in Flask, we can clone a project and run pip3 install -r requirements.txt which will read and install the dependencies in requirements.txt.

##Create a .gitignore file and enter the following lines inside it:
1. .env
1. *.sqlite
1. *.pyc
This prevents our environment directory, any sqlite database files, and any pycache files from being tracked by git.

###Setting up a basic server
1. Create a file called app.py.
###To run our server, we will run this command:
1. python3 app.py

###Create A Model
1. Set up a Cloud model with three properties: "name", "genus", and "form_level".
1. Setting up a model
1. Peewee: A Flask ORM
1. Peewee is a simple and small ORM. It has few (but expressive) concepts, making it intuitive to use. — from the Peewee documentation

1. This is the ORM (Object-relational model, or Object-relational mapping) that we will use to connect to our SQL databases in order to query them.

1. Create a file called models.py.

###Setting up a resource
1. In Flask we will use resources instead of controllers.

###Resource: 
1. The main building block provided by Flask-RESTful are resources, which gives us access to our HTTP methods just by defining methods on your resource. A basic CRUD source looks like the @app.route('/') block in app.py.

##BluePrints: 
1. The basic concept of blueprints is that they record operations to execute when registered on an application. Flask associates view functions with blueprints when dispatching requests and generating URLs from one endpoint to another.

1. A view function, or view for short, is a Python function that takes a Web request and returns a Web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really. The view itself contains whatever arbitrary logic is necessary to return that response (from the Django documentation).

##Create a folder called resources.
1. Inside that folder, create files called __init__.py and dogs.py.