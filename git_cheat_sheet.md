## **Git Set Up**

1. `$ cd`  into the folder you want to clone your project into
2. `$ git clone`  followed by the link to your project repo
3. Projects are not tracked with Git (and therefore don't use Git) until it is initialized as a Git project. To turn any folder into a Git project, run this command in the project root: `$ git init`

## **Git Workflow**

1. Confirm that the project is in the state you expect with `$ git status`
4. Determine what your next task or goal is.
5. Start running tests, writing code, etc.
6. When you have a small, meaningful change, get ready to make a commit:
    1. Move the intended changes from local changes area to staging with `git add name_of_file.py or $ git add -p` `git add .` 
    2. Create a commit and a commit message from the changes in staging with `$ git commit -m ""`
    3. Review the commit with `$ git show`
7. Create at least one commit. Continue to write code and make commits.
8. Fetch and merge any new commits from `origin` with `$ git pull`
9. Review the code; check that the tests still pass, and the code still runs
    - If the code is broken, restart this process and make commits that will fix the problem
10. Send all of your commits to `origin` with `$ git push`
11. Review your work with `$ git status` and `$ git **log