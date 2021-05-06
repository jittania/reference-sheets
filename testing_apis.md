## **Environment Variables**

From any terminal prompt, we can run the command env. This displays the environment variables currently set in our terminal

    $ export MY_NEW_VAR="my value"

---

## **Steps for...something**

1. Ensure that `python-dotenv` is installed by checking requirements.txt 

2. Create a dotenv .env file

    $ touch .env

3. Prevent our .env from being committed by using a .gitignore file by adding `.env` file to `.gitignore` in text editor on its own line, IF it's not already there

4. Create/populate environment variables in our `.env` file:

    VARIABLE_NAME = <variable value>

5. Create a test database with the same name as the test you want to create

6. Refactor our create_app method to check for a configuration flag and read the correct database location from .env


        from flask import Flask
        from flask_sqlalchemy import SQLAlchemy
        from flask_migrate import Migrate

        # The python-dotenv package specifies to import the package like this:
        from dotenv import load_dotenv
        # This built-in module provides a way to read environment variables:
        import os

        db = SQLAlchemy()
        migrate = Migrate()
        # this loads the values from our .env file so that the os module is able to see them:
        load_dotenv()

        # added new parameter test_config which has a default value of None, making it optional:
        def create_app(test_config=None):
            app = Flask(__name__)

            if not test_config:
                app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
                app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
                    "SQLALCHEMY_DATABASE_URI")
            else:
                # The following line with True turns testing mode on:
                app.config["TESTING"] = True
                app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
                app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
                    "SQLALCHEMY_TEST_DATABASE_URI")

            db.init_app(app)
            migrate.init_app(app, db)

            from app.models.book import Book

            from .routes import books_bp
            app.register_blueprint(books_bp)

            return app

  
7. Manually test that our development environment still works


---

## **Super Extra Simple Fixture/Test Example:**

The following declares a fixture and a test that uses it:

    @pytest.fixture
    def my_fixture():
        pass

    def test_my_fixture(my_fixture):
        pass

## **Creating Basic Fixtures**

    import pytest

    @pytest.fixture
    def empty_list():
        return []

    def test_len_of_empty_list(empty_list):
        assert isinstance(empty_list, list)
        assert len(empty_list) == 0

## **Creating Fixtures With Dependencies**

    @pytest.fixture
    def one_item(empty_list):
        empty_list.append("item")
        return empty_list

    def test_len_of_unary_list(one_item):
        assert isinstance(one_item, list)
        assert len(one_item) == 1
        assert one_item[0] == "item"

## **Creating Fixtures With Cleanup**

    # Declares a class that has "setup" code (in __init__), and "cleanup" code (in cleanup)
    class FancyObject:
        def __init__(self):
            self.fancy = True
            print(f"\nFancyObject: {self.fancy}")

        def or_is_it(self):
            self.fancy = not self.fancy

        def cleanup(self):
            print(f"\ncleanup: {self.fancy}")

    @pytest.fixture
    def so_fancy():
        # Creates a new FancyObject instance, which runs the code in the __init__ function. The instance is assigned to the fancy_object variable:
        fancy_object = FancyObject()

        # returns fancy_object to test and waits for test to finish (paused on this line of code):
        yield fancy_object

        # proceeds with the clean up only when the so_fancy function resumes
        fancy_object.cleanup()

    def test_so_fancy(so_fancy):
        assert so_fancy.fancy
        so_fancy.or_is_it()
        assert not so_fancy.fancy

---

## Test Set up

Create a tests folder (in the project directory), and the following files:

tests/__init__.py
tests/conftest.py
tests/test_routes.py

File | Responsibility of this file
---- | ----
`__init__.py` | Establishes our tests package, so it can be properly connected with the rest of the app folders and files. We will leave it empty, as we typically do.
`conftest.py` |	A standard pytest file that holds test configurations and common test helper functions. Essentially, this file is run before any other test files. This allows fixtures registered here to be available to any other test file. This is usually where we'll deifne fixtures
`test_routes.py` |	This file will hold the tests for the code in our app/routes.py file.

### **`conftest.py`**

    import pytest
    from app import create_app
    from app import db


    @pytest.fixture
    def app():
        app = create_app({"TESTING": True})

        with app.app_context():
            # creates test database in test environment 
            db.create_all()
            # returns instance of app to the test and pauses:
            yield app

        with app.app_context():
            # drops test database
            db.drop_all()

    @pytest.fixture
    # This fixture is named client. It will request the existing app fixture to run, first:
    def client(app):
        # The responsibility of this fixture is to make a test client, which is an object able to simulate a client making HTTP requests.
        return app.test_client()

---

## **Using Tests:**

### **Basic Test Example**

    # We pass in the client fixture here, which we registered in conftest.py. pytest automatically tries to match each test parameter to a fixture with the same name.
    def test_get_all_books_with_no_records(client):
        # Act
        # This sends an HTTP request to /books. It returns an HTTP response object, which we store in our local variable response
        response = client.get("/books")
        # We can get the JSON response body with response.get_json()
        response_body = response.get_json()

        # Assert
        assert response.status_code == 200
        assert response_body == []

### **Adding Test Data with Fixtures**

    def test_get_one_book(client, two_saved_books):
        # Act
        response = client.get("/books/1")
        response_body = response.get_json()

        # Assert
        assert response.status_code == 200
        assert response_body == {
            "id": 1,
            "title": "Ocean Book",
            "description": "watr 4evr"
        }


**Then run the tests! (in a virtual environment)**