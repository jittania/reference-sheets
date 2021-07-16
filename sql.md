
[Markdown Syntax Guide](https://www.markdownguide.org/basic-syntax/)


## **Importing SQL Files**

    psql -U postgres -d intro_to_sql_problem_set < RELATIVE/PATH/TO/THIS/FILE/intro-to-sql-problemset.sql

where `RELATIVE/PATH/TO/THIS/FILE/intro-to-sql-problemset.sql` is the relative path to the downloaded .sql file  
  

We can read this whole command as
1. `psql`: "Start the psql repl"
2. `-U postgres`: "As the user named postgres"
3. `-d intro_to_problem_set`: "automatically connect me to a database named intro_to_problem_set"
4. `<` : Put something into that database
5. `RELATIVE/PATH/TO... .sql`: Put into the database this specific file

Therefore, the last argument should be a path where your current terminal location can access that downloaded sql file!

---

## **Interacting With Databases and Tables**

syntax | meaning
--- | ---
`psql -U postgres` | opens the Postgres interactive terminal with a Postgres user named `postgres`
`\l` | list all available Postgres databases on this machine
`\c db_name` | connect to a database
`\dt` | (must be connected to a database first!!) view a list of all tables that are within the connected database

## **Creating and Deleting**

Syntax | Action
---- | ----
`CREATE DATABASE db_name;` | create a datebase
`DROP DATABASE db_name;` | delete a database 
`CREATE TABLE example_table_name (column_name data_type constraint_name, column_name data_type constraint_name);` | create a table (generic syntax)
`CREATE TABLE example_table_name (column_name data_type PRIMARY KEY, column_name data_type constraint_name);` | create a table with columns and a primary key
`CREATE TABLE example_table_name (column_name INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, column_name data_type constraint_name);` | create a table with an auto-incrementing primary key   
`DROP TABLE example_table_name;` | delete a table

## **Managing Records**

Syntax | Action
---- | ----
`INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);` | add a record
`SELECT column1, column2, column3, ... FROM table_name;` | get specific columns from all records within a specific table
`SELECT * FROM table_name;` | get all columns and all records from a specific table
`UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;` | update a record
`DELETE FROM table_name WHERE condition;` | delete a record

## **Modifying Tables**

Syntax | Action
---- | ----
`ALTER TABLE table_name ADD COLUMN column_name data_type constraint_name;` | adds a new column
`ALTER TABLE table_name DROP COLUMN column_name;` | removes a column
`ALTER TABLE table_name ALTER COLUMN column_name TYPE new_data_type USING conversion_expr;` | modifies data type of a column
`ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;` | renames a column
`ALTER TABLE table_name RENAME TO new_table_name;` | renames a table

## **Modifying Databases**

Syntax | Action
---- | ----
`ALTER DATABASE database_name RENAME TO new_database_name;` | renames a database

## **Filtering and Ordering Records**

Syntax | Action
---- | ----
`SELECT columns_desired FROM table_name (additional optional clauses) ORDER BY sort_expression1 sort_direction, ... ;` | using `ORDER BY` to sort the results of a query
`SELECT title, price FROM books ORDER BY price DESC;` | using `ORDER BY` and `DESC` to sort the results of a query in descending order
`SELECT title, price FROM books ORDER BY price NULLS LAST;` | put any row with a price of `NULL` last in the results (by default, `ORDER BY` will put `NULL` values first)
`SELECT columns_desired FROM table_name (additional optional clauses) LIMIT row_count;` | retrieiving a specific number of rows from a `SELECT` query
`SELECT title FROM books WHERE genre = 'sci-fi' LIMIT x OFFSET n;` | adding an offset to a `LIMIT` clause, outputting a total of x records while bypassing the first n records
`SELECT title, price FROM books ORDER BY price DESC LIMIT n;` | combining `ORDER BY` and `LIMIT` to sort our records and then retrieving a subset of those sorted records

## **Foreign Keys And Joining Tables**

Syntax | Action
---- | ----
`CREATE TABLE table_name (column_name data_type PRIMARY KEY, column_name data_type constraint_name, FOREIGN KEY (foreign_key_id) REFERENCES other_table_name(id));` | connects a row in one table with one or many rows in another (one-to-one or one-to-many). Translating the last line: "this table has a foreign key column named `foreign_key_id` that references the `id` column in the table `other_table_name`"
`CREATE TABLE books_genres (book_id INT, FOREIGN KEY (book_id) REFERENCES books(id), genre_id INT, FOREIGN KEY (genre_id) REFERENCES genres(id), PRIMARY KEY (book_id, genre_id));` | creates a join table between two tables, using the books and genres example (many-to-many relationship). The last expression is saying that the primary key for this table is the combo of the primary keys from both tables
`SELECT field1, field2, field3, ...FROM table_name_a INNER JOIN table_name_b ON condition/* Optional WHERE clause */` |  using `INNER JOIN` to combine (join) and return all the rows in both tables which possess matching keys. Field names should be comma-separated, and often take the form of `table_name.column_name`. The conditional expression determines how the rows will be matched between the two tables