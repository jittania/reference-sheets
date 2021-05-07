# **CRUD!!!!**

## **Example: Creating an Endpoint**

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
`list_sorted_by_col_attribute = Model_name.query.order_by(asc(Model_name.col_attribute))` | must include `from sqlalchemy import asc` in file. Assumes table with model_name already migrated. Also works with `desc` 


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

