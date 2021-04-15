## Summary of one-time project setup:

1. `cd` into your `projects` folder
2. Clone the project onto your machine with `git clone project-url`
3. `cd` into the project's root directory
4. Create the virtual environment `venv`
    `python3 -m venv venv`
5. Activate the virtual environment `venv`
    `source venv/bin/activate`

    Verify that you're in a python3 virtual environment by running:

    `python --version` should output a Python 3 version
    `pip --version` should output that it is working with Python 3

6. Install the dependencies with pip
    `pip install -r requirements.txt`

## Getting Code onto GitHub the First Time

1. Go into your project folder $ cd project-name
2. Confirm that your project was a fork from the original project repo:
    - Run $ git remote -v
    - Confirm that origin has a value of your own project repo. Your GitHub username should be in the path of origin
3. Make a commit with all of the project files:
    - Add all files to staging with $ git add -A
    - Make a commit with a meaningful commit message $ git commit -m "Your message here"
4. Push your project commit to your own project repo
    - Run $ git push or $ git push origin master

## How to Make a Pull Request

1. Go to your project repo on GitHub, typically https://github.com/<your-username>/<project-name>
2. Navigate to the Pull Requests tab
3. Begin a new pull request by clicking "New Pull Request"
4. Configure this PR so it compares your project against Ada's:
    - base repository is <some-ada-repo>/<project-name>
    - base is master
    - head repository is <your-username>/<project-name>
    - compare is master
5. Add more details by clicking "Create pull request" 
6. Finish this PR by clicking "Create pull request"
7. Grab the URL of this PR, typically https://github.com/<some-ada-repo>/<project-name>/pulls