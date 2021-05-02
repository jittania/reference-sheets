## **Flask Set up**

At the beginning of the project, or after any updates to this file, we install all dependencies with (have to be in virtual environment!):

    (venv) $ pip install -r requirements.txt

To update the requirements.txt file, we use this command:

    (venv) $ pip freeze > requirements.txt

## **Server Commands**

Syntax | Action
--- | ---
`(venv) $ flask run` | runs a Flask server
`(venv) $ FLASK_ENV=development flask run` | runs a Flask server in Debug mode so that we don't need to restart the server after each change 
`(venv) $ export FLASK_ENV=development` | switch to dev mode if Flask is already running
`(venv) $ FLASK_ENV="development" && flask run` |
CTRL + C | stops a Flask server


   
---

## **Recommended Project Structure**
    .
    ├── app
    │   ├── models              # holds data models
    │   │   └── __init__.py     
    │   ├── __init__.py         # contains startup code for our app
    │   └── routes.py           # define endpoints here
    ├── README.md
    └── requirements.txt



## **Creating Blueprints and Endpoints**

**Creating a Blueprint in `app/routes.py`**:

    from flask import Blueprint

    hello_world_bp = Blueprint("hello_world", __name__)


**Registering a Blueprint in `app/__init__.py`**:

    from flask import Flask

    def create_app(test_config=None):
        app = Flask(__name__)

        from .routes import hello_world_bp
        app.register_blueprint(hello_world_bp)

        return app


**Defining an endpoint in `app/routes.py`**:

    @blueprint_name.route("/endpoint/path/here", methods=["GET"])
    def endpoint_name():
        my_beautiful_response_body = "Hello, World!"
        return my_beautiful_response_body

## **Debugging Strategies**

1. Check server logs in Terminal
2. If you have Flask in Developer mode, you'll get more information when you bring up the endpoints in a browser or in Postman. it also means it will automatically reload the server every time you save to a file. 
3. You can use the VS Code Debugger with Flask!


---

## **Setting up Models in Flask**
    .
    ├── app
    │   ├── models
    │   │   ├── __init__.py
    │   │   └── model.py
    │   ├── __init__.py
    │   └── routes.py
    ├── README.md
    └── requirements.txt

1. **Set up the database for the project** - create a database in Terminal

    $ psql -U postgres

    $ CREATE DATABASE hello_books_development;


2. **Configure our app to connect to the database** - Flask needs a way to connect to our database. We'll do so by providing a path to it in `app/__init__.py`

Connection string template: `postgresql+psycopg2://postgres:postgres@localhost:5432/REPLACE_THIS_LAST_PART_WITH_DB_NAME`. This tells Flask to connect to our database using the `psycopg2` package we installed from our `requirements.txt`. It connects using the `postgres` protocol using the `postgres` user on the local machine running at port `5432`.

        # Imports and sets up the packages SQLAlchemy and Migrate (a companion package to SQLAlchemy)
        from flask import Flask
        from flask_sqlalchemy import SQLAlchemy
        from flask_migrate import Migrate

        # Sets up db and migrate, which are conventional variables that give us access to database operations
        db = SQLAlchemy()
        migrate = Migrate()

        def create_app(test_config=None):
            app = Flask(__name__)

            # Configures the app: connects the database and flask
            app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

            # Connects db and migrate to our Flask app
            db.init_app(app)
            migrate.init_app(app, db)

            return app


3. **Define our model in Python code** - We will create a class for each model. The class will define the state and behavior of our model. Make sure the model has its own .py file; then, to define the model, put inside `app/models/book.py` :

        # This file needs access to the SQLAlchemy db
        from app import db

        # Define a new class named after our model, which will inherit from db.Model, and will have these 3 columns
        class Book(db.Model):
            # Creates an attribute id, which will map to a database column (which will be the primary key, an integer and will autoincrememnt)
            id = db.Column(db.Integer, primary_key=True, autoincrement=True)

            # Creates a title attribute, which will map to a string column, title
            title = db.Column(db.String)

            # Creates a description attribute, which will map to a string column, description
            description = db.Column(db.String)



4. **Ensure that Flask and SQLAlchemy are able to see our model code** 

Making the `Book` Model Visible during the `app` start-up by adding this code to  `__init__.py`:

        def create_app(test_config=None):
                # app = Flask(__name__)
                # ... app is configured with SQLAlchemy settings
                # ... db and migrate are initialized with app

                # must place the following AFTER db and migrate are initialized, but BEFORE the return app statement:
                from app.models.book import Book

            return app


5. **Use tools to convert the model into instructions for creating or updating tables**
6. **Apply the instructions to our database to create or update the tables**

---

## **Database Migrations Workflow**

1. **Set up the database on the Flask end once - this tells Flask how to connect to the database**

    (venv) $ flask db init


2. **Generate migration files (after each model change) - which are instructions on how to set up the structure of the database with tables, columns, their names, etc**

    (venv) $ flask db migrate -m "put a message here describing what it's doing"


3. **Apply the migration files (after each model change) - runs the migrations that you made and puts those changes in place**

    (venv) $ flask db upgrade

Confirm successful migration by connecting to Postgres, then connecting to database 


## **Dev Workflow**

Our modified dev workflow for Flask development may now look like this:

1. `cd` into a project root folder
2. Activate a virtual environment
3. Check git status
4. Start the server
5. Cycle frequently between:
    1. Writing code
    2. Checking git statuses and making git commits
    3. Debugging with Postman, server logs, VS Code, and more
6. Stop the server
7. Deactivate the virtual environment

