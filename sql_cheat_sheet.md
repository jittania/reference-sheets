`psql -U postgres` | open postgres terminal

`psql -U postgres -d name_of_database < name_of_file.sql` | import a file (note that you must be in the same directory as the file (and exited out of postgres) for this command to work)




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