
## Importing SQL Files

    psql -U postgres -d intro_to_sql_problem_set < RELATIVE/PATH/TO/THIS/FILE/intro-to-sql-problemset.sql

where `RELATIVE/PATH/TO/THIS/FILE/intro-to-sql-problemset.sql` is the relative path to the downloaded .sql file

We can read this whole command as
1. `psql`: "Start the psql repl"
2. `-U postgres`: "As the user named postgres"
3. `-d intro_to_problem_set`: "automatically connect me to a database named intro_to_problem_set"
4. `<` : Put something into that database
5. `RELATIVE/PATH/TO... .sql`: Put into the database this specific file

Therefore, the last argument should be a path where your current terminal location can access that downloaded sql file!

## Interacting With Databases and Tables

syntax | meaning
--- | ---
`\l` | list all available Postgres databases on this machine
`\c db_name` | connect to a database
`\dt` | (must be connected to a database first!!) view a list of all tables that are within the connected database

## Creating databases
    CREATE DATABASE db_name;

## Deleting databases
    DROP DATABASE db_name; 

## Creating Tables

### General syntax:
    CREATE TABLE example_table_name (
        column_name data_type constraint_name,
        column_name data_type constraint_name
    );

### Create a table with columns and a primary key:
    CREATE TABLE example_table_name (
        column_name data_type PRIMARY KEY,
        column_name data_type constraint_name
    );

### Create a table with an auto-incrementing primary key:
    CREATE TABLE example_table_name (
        column_name INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        column_name data_type constraint_name
    );   

## Deleting Tables
    DROP TABLE example_table_name;

## Adding Records
    INSERT INTO table_name (column1, column2, column3, ...)
    VALUES (value1, value2, value3, ...);

## Retrieving Records

### Specific columns from all records within a specific table:
    SELECT column1, column2, column3, ... FROM table_name;

### Get all columns and all records from a specific table:
    SELECT * FROM table_name;

## Updating Records
    UPDATE table_name
    SET column1 = value1, column2 = value2, ...
    WHERE condition;

## Deleting Records
    DELETE FROM table_name
    WHERE condition;