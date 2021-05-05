## **Flask Project One-time Set Up**

1. Fork and clone, `cd` into project root folder
2. Create virtual environment
3. At the beginning of the project, OR after any updates to this file, install all dependencies with (have to be in virtual environment!):

    (venv) $ pip install -r requirements.txt

To update the requirements.txt file, we use this command:

    (venv) $ pip freeze > requirements.txt

4. Start the Flask server

Syntax | Action
--- | ---
`(venv) $ flask run` | runs a Flask server
`(venv) $ FLASK_ENV=development flask run` | runs a Flask server in Debug mode so that we don't need to restart the server after each change 
`(venv) $ export FLASK_ENV=development` | switch to dev mode if Flask is already running
`(venv) $ FLASK_ENV="development" && flask run` |
CTRL + C | stops a Flask server


## **Flask Project Workflow**

Our modified dev workflow for Flask development may now look like this:

1. `cd` into a project root folder
2. Activate a virtual environment
3. Check git status and pull down commits 
4. Update local database using `flask db upgrade`
5. Start the server
6. Cycle frequently between:
    1. Writing code
    2. Checking git statuses and making git commits
    3. Debugging with Postman, server logs, VS Code, and more
7. Stop the server
8. Deactivate the virtual environment
   
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

---

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

## **Setting up Models in Flask: An Overview**
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

## **Database Migrations Overview**

1. **Set up the database on the Flask end once - this tells Flask how to connect to the database**

    (venv) $ flask db init


2. **Generate migration files (after each model change) - which are instructions on how to set up the structure of the database with tables, columns, their names, etc**

    (venv) $ flask db migrate -m "put a message here describing what it's doing"


3. **Apply the migration files (after each model change) - runs the migrations that you made and puts those changes in place**

    (venv) $ flask db upgrade

Confirm successful migration by connecting to Postgres, then connecting to database 

---


## **Example : Creating an Endpoint**

### **Preparation:**

Identify the following based on the given prompt:
   - the HTTP Method (in this case, `POST`)
   - Endpoint
   - Request body
   - Appropriate successful response status code 

### **Write Code:**

Adding to `routes.py`:
        # import the necessary modules for our Book model
        from app import db
        from app.models.book import Book

        # We need to import our dependencies. Python supports comma-separated importing.
        from flask import request, Blueprint, make_response

        # Our Blueprint instance. We'll use it to group routes that start with /books.
        books_bp = Blueprint("books", __name__, url_prefix="/books")

        # A decorator that uses the books_bp Blueprint to define an endpoint and accepted HTTP method
        @books_bp.route("", methods=["POST"])
        # This function will execute whenever a request that matches the decorator is received
        def handle_books():
            # get the request body as a Python dictionary 
            request_body = request.get_json()
            # making a new book 
            new_book = Book(title=request_body["title"],
                            description=request_body["description"])
            # we want the database to add new_book (staging)
            db.session.add(new_book)
            # we want the database to save and commit the collected changes
            db.session.commit()

            # For each endpoint, we must return the HTTP response
            return make_response(f"Book {new_book.title} successfully created", 201)


### **Register a Blueprint:**
Then, we must register the blueprint within our `create_app` function in `app/__init__.py`. 

        def create_app():
            app = Flask(__name__)

            # ... existing code that did
            # app config...
            # db initialization...
            # migrate initialization...
            # import models...
            # create the models...

            from .routes import books_bp
            app.register_blueprint(books_bp)

            # ... return app

---

## **Example: Updating an Endpoint**

### **Preparation:**

Identify the following based on the given prompt:
   - the HTTP Method (in this case, `PUT`)
   - Endpoint
   - Request body
   - Appropriate successful response status code 

### **Write Code:**
    # This route's matching methods now need to be updated to handle PUT requests
    @books_bp.route("/<book_id>", methods=["GET", "PUT"])
    def handle_book(book_id):
        book = Book.query.get(book_id)

        if request.method == "GET":
            # ... existing code that returned a dictionary
        elif request.method == "PUT":
            form_data = request.get_json()

            book.title = form_data["title"]
            book.description = form_data["description"]

            db.session.commit()

            return make_response(f"Book #{book.id} successfully updated")


---

## **Example: Deleting an Endpoint**

### **Preparation:**

Identify the following based on the given prompt:
   - the HTTP Method (in this case, `DELETE`)
   - Endpoint
   - No request body needed for deleting an endpoint
   - Appropriate successful response status code 

### **Write Code:**

    @books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
    def handle_book(book_id):
        book = Book.query.get(book_id)

        if request.method == "GET":
            # ... existing code for getting a single book
        elif request.method == "PUT":
            # ... existing code for updating a single book
        elif request.method == "DELETE":
            db.session.delete(book)
            db.session.commit()
            return make_response(f"Book #{book.id} successfully deleted")


---

## **Example: Finding, Updating, Deleting, etc a Missing Book**

"As a client, I want to send a request trying to get one non-existing book and get a 404 response, so I know that the book resource was not found." 

In other words, the endpoint will need to:

1. Read the `book_id` in the request path
2. Retrieve the book with the matching `book_id` from the db
3. Discover that there is no matching book with `book_id` in the db
4. Send back a response

### **Preparation:**

Identify the following based on the given prompt:
   - the HTTP Method (in this case, `GET`)
   - Endpoint (can use our existing endpoint that reads a record, but using an invalid id)
   - No request body needed for `GET` requests
   - Appropriate successful response status code (`404 Not Found`)


### **Write Code:**

1. **Just for one endpoint with a specific verb(s)**

    @books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
    def handle_book(book_id):
        book = Book.query.get(book_id)

        if request.method == "GET":
            if book is None:
                return make_response("", 404)
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        # ... existing code for updating a single book
        # ... existing code for deleting a single book

2. **Can also just add a `None` check before checking for verb**

    @books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
    def handle_book(book_id):
        book = Book.query.get(book_id)
        if book is None:
            return make_response("", 404)

        if request.method == "GET":
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        # ... existing code for updating a single book
        # ... existing code for deleting a single book

---

## **Even More Query Stuff**

Syntax | Action
------ | ------
`Book.query.filter_by(title="Fictional Book Title")` | use give keyword arguments to describe the attribute and value on which we're filtering
`Book.query.limit(100).all()` |  limit the number of results in our queries
`query_param_value = request.args.get(query_param_key)` | using the `request.args` object to get the value from any query param and assign it to a variable `query_param_value`


---

## **Example: Using Query Params** 

"As a client, I want to send a request trying to get a list of books with a matching title, so I know which books have a matching title."

In other words, the endpoint will need to:

1. Check if the HTTP method is GET
2. Check if we have a query param for title
3. If we have a title query param, retrieve all of the books from the database that match, otherwise retrieve all books as usual
4. Format the books data into the appropriate structure (list of dictionaries, where each dictionary has id, title, and description)
5. Send back a response

### **Preparation:**

Identify the following based on the given prompt:
   - the HTTP Method (in this case, `GET`)
   - Endpoint (`/books?title=Apples`)
   - No request body needed for `GET` requests
   - Appropriate successful response status code (`200 OK` for the response status code, and a JSON response body representing a list of books)


### **Write Code:**

    @books_bp.route("", methods=["GET", "POST"])
    def handle_books():
        if request.method == "GET":
            # this code replaces the previous query all code
            title_query = request.args.get("title")
            if title_query:
                books = Book.query.filter_by(title=title_query)
            else:
                books = Book.query.all()
            # end of the new code



---

### **Manually Test Code:**

First - make sure Flask is running! Use `FLASK_ENV=development flask run`

**With Postman**:

1. Set the method 
2. Set the request URL 
3. Configure an HTTP response body to raw and JSON, and add in the sample request body

**With `psql`**:

1. Start up `psql` with `psql -U postgres`
2. Connect to  database with `\c db_name`
3. Run an appropriate query to get the records from the `book` table, such as `SELECT * FROM table_name`


---



