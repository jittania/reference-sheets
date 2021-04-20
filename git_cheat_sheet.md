## **Git Set Up**

1. `$ cd`  into the folder you want to clone your project into
2. `$ git clone`  followed by the link to your project repo
3. Projects are not tracked with Git (and therefore don't use Git) until it is initialized as a Git project. To turn any folder into a Git project, run this command in the project root: `$ git init`

## **Git Workflow**

1. Confirm that the project is in the state you expect with `$ git status`
4. Determine what your next task or goal is.
5. Start running tests, writing code, etc.
6. When you have a small, meaningful change, get ready to make a commit:
    1. `cd` into project
    2. Move the intended changes from local changes area to staging with 
         - `git add name_of_file.py` (just adding one file)
         - `git add .` (to select all files under the current directory)
         - `git add -p` 
            - This starts an interactive mode where local code changes will be presented on the screen one at a time.
            - At each chunk, we can decide whether the change should go into staging: `y` then enter for "yes," `n` then enter for "no."
            - This mode cycles through all chunks in the local changes area, then exits the interactive mode
            - This method encourages reviewing code changes
    1. Create a commit and a commit message from the changes in staging with `git commit -m ""`
    2. Review the commit with `git show`, then exit that view and get back to command line with `q`
7. Create at least one commit. Continue to write code and make commits.
        - Commits are always made against your local Git repository, so you don’t have to worry about the commit being perfect or ready to share with others.
8. Fetch and merge any new commits from `origin` with `git pull`
9.  Review the code; check that the tests still pass, and the code still runs
    - If the code is broken, restart this process and make commits that will fix the problem
10. Send all of your commits to `origin` with `git push`
11. Review your work with `git status` and `git log`

## Version Controlling with Git in Visual Studio Code

1. From VS Code: Press Ctrl+Shift+P to show the Command Palette

2. Execute the "Git: Clone command". It may help to type “Git” to bring it to the shortlist. Select a local path to clone the repo to. Open the cloned repository

3. Committing changes:

      1. Select the Source Control tab
      2. Enter a commit message of “My commit” and press Ctrl+Enter to commit it locally.
      3. If asked whether you would like to automatically stage your changes and commit them directly, click Always
      4. Click the Synchronize Changes button to synchronize your changes with the server. Confirm the sync if prompted.

4. Working with branches:

    Note: Committing changes to a branch will not affect other branches and you can share branches with others without having to merge the changes into the main project. You can also create new branches to isolate changes for a feature or a bug fix from your master branch and other work.

    **Creating a new branch in your local repository:**
      1. Navigate to the "Source Control" window (the branch icon) 
      2. Select the master branch
      3. Select "Create new branch from" and enter a name
      4. Select the master as the reference branch.
      5. You are now working on that branch.



