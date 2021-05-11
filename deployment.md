# **Initial Deployment To Heroku** 

1. **Configure our Flask project(app) for Heroku**

Check Dependencies for `gunicorn`

Create a Procfile for Heroku with the following content:

    web: gunicorn 'app:create_app()'

2. **Commit our new configurations**

3. **Create a Heroku app via the CLI**

Create a Heroku app with an automatically generated app name using

    $ heroku create

...OR create our app with the name `your-app-name` using:
    

    $ heroku create your-app-name

Confirm that we have a heroku remote by running this command:

    $ git remote -v

Then verify in the Heroku dashboard that app was created 

4. **Push code to the Heroku remote**

The push command will very depending on how you have branches set up, but generally speaking:

    $ git push heroku <branch on computer>:<branch name on heroku>

5. **Create a database in Heroku via the CLI**

This command uses the Heroku CLI to add a Postgres database to the app:

    $ heroku addons:create heroku-postgresql:hobby-dev

Then verify that our Heroku app has added a Postgres database by checking the Heroku dashboard  

6. **Set the environment variables for Heroku**




7. **Setup and initialize the database in Heroku via the CLI**

The following command will migrate the empty database in our remote Postgres connection to the latest schema configuration we have generated from our models:

    $ heroku run flask db upgrade

1. **Verify**

Run this command inside of project folder to automatically opne the app in the browser:

    $ heroku open


Access the server logs using the Heroku CLI and running:

    $ heroku logs


To see the logs output in real time, run:

    $ heroku logs --tail

use this to execute psql commands, and check, add, update, or delete the data that our app uses:

    $ heroku pg:psql

---

## Troubleshooting stuff

- If the command `heroku run flask db upgrade` creates an error, try this:
        1. Delete migrations folder entirely from project repo
        2. Connect to local project database (for example, task_list_api_development) and delete all tables from that database (including alembic)
        3. Run migrations again with `flask db init`, `flask db migrate`, `flask db upgrade`
        4. Add and commit changes (standard git syntax), then push to heroku with `git push heroku <current_branch>:main`
        5. Now try `heroku run flask db upgrade` again

# **Subsequent Deployment**