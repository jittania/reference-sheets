## **Git Set Up**

### **If you already have a remote repo set up on GitHub:**

1.  Create a local folder for project 
2.  `git clone`  followed by the link to your GitHub project repo

### **If you've already created a project repo locally and want to put a remote repo on GitHub:**

1.  Projects are not tracked with Git (and therefore don't use Git) until it is initialized as a Git project. To turn any folder into a Git project, run this command in the project root: `git init`
2.  Create an empty repo on GitHub
3.  Link the local repository to an empty GitHub repository using the following command: `git remote add origin [url]`

---

## **Git Workflow - Solo Project**

1. Confirm that the project is in the state you expect with `git status`
4. Determine what your next task or goal is.
5. Start running tests, writing code, etc.
6. When you have a small, meaningful change, get ready to make a commit:
    1. `cd` into project
    2. Move the intended changes from local changes area to staging with 
         - `git add name_of_file` (adding specific file(s))
         - `git add .` (to select all files under the current directory)
         - `git add -p` 
            - This starts an interactive mode where local code changes will be presented on the screen one at a time.
            - At each chunk, we can decide whether the change should go into staging: `y` then enter for "yes," `n` then enter for "no."
            - This mode cycles through all chunks in the local changes area, then exits the interactive mode
            - This method encourages reviewing code changes
    3. Create a commit and a commit message from the changes in staging with `git commit -m ""`
    4. Review the commit with `git show`, then exit that view and get back to command line with `q`
7. Create at least one commit. Continue to write code and make commits.
        - Commits are always made against your local Git repository, so you don’t have to worry about the commit being perfect or ready to share with others.
8. Fetch and merge any new commits from `origin` with `git pull` 
    - If pulling from a particular branch other than `main`, use `git pull origin <branch pulling FROM>`
9.  Review the code; check that the tests still pass, and the code still runs
    - If the code is broken, restart this process and make commits that will fix the problem
10. Send all of your commits to `origin` with `git push`, or for more specificity, use:
    -  `git push origin BRANCH-NAME` 
    -  or, if pushing from one branch to another (usually `main`), `git push <repo name> <from this branch>:<to this branch>`
11. Review your work with `git status` and `git log`

---

## **Moar Git Commands**
Syntax | Action
--- | ---
`git status` | lists the uh, status
`git branch` | lists existing branches 
`git switch <destination-branch-name>` | switch to an existing branch (new)
`git checkout <existing_branch>` | switch to an existing branch (old-school)
`git branch <new-branch-name>` | create a new branch
`git checkout -b <new_branch>` | create a new branch and switch to it
`git branch -m <new_name>` | rename a LOCAL branch. must be on the branch that you want to rename 
`git branch -d localBranchName` | delete branch locally
`git push origin --delete remoteBranchName` | delete branch remotely
`git diff HEAD` | after a `git add` command, this command will list show the changes made since most recent commit
`git remote` | Shows names of remote repositories 
`git remote -v` | Shows names and URLs of remote repositories 
`git config --global push.default current` | One-time optional commnand!! This will ensure that when you run only git push without specifying the branch name, it will push to the remote repo from the local machine’s existing branch to the same branch in remote repo. That is, it should pushes the current branch to update a branch with the same name on the receiving end.
`git push <repo name> <branch name>` | general syntax for pushing to specific repo and branch
`git push <repo name> <from this branch>:<to this branch>` | optional syntax for pushing from one branch to another
`git reset --soft HEAD~1` | The easiest way to undo the last Git commit is to execute the “git reset” command with the “–soft” option that will preserve changes done to your files. You have to specify the commit to undo which is “HEAD~1” in this case (“HEAD~1” means that you want to reset the HEAD (the last commit) to one commit before in the log history)


---

## **Version Controlling with Git in Visual Studio Code**

1. From VS Code: Press Ctrl+Shift+P to show the Command Palette

2. Execute the "Git: Clone command". It may help to type “Git” to bring it to the shortlist. Select a local path to clone the repo to. Open the cloned repository.

3. Committing changes:

      1. Select the Source Control tab
      2. Enter a commit message of “My commit” and press Ctrl+Enter to commit it locally.
      3. If asked whether you would like to automatically stage your changes and commit them directly, click Always
      4. Click the Synchronize Changes button to synchronize your changes with the server. Confirm the sync if prompted.

4. Working with branches:

    Note: Committing changes to a branch will not affect other branches and you can share branches with others without having to merge the changes into the main project. You can also create new branches to isolate changes for a feature or a bug fix from your master branch and other work.

    **Creating a new branch in your local repository:**
      1. Navigate to the "Source Control" window (the branch icon) 
      2. Look at the far left corner of the blue status bar at the bottom of the screen, which tells you which branch you're working on (you can click on it directly to change it) - make sure it's on "master branch"
      4. Select "Create new branch from" and enter a name
      5. Select the master as the reference branch.
      6. You are now working on that branch.



---

## **Git Workflow - Group Project**

*From Merge Conflict Carnival activity*

"Once everyone in your group has completed the baseline setup instructions above you're ready to start building the recipe together. Because each member of your group now has a different version of the recipe file in their local repository, building the complete recipe by merging those versions together will result in merge conflicts. To handle those merge conflicts sensibly your group should use the following process to construct the final recipe file:"

1. Pull with `git pull origin <branch pulling FROM>`
2. Each person on a team will create a branch with `git checkout -b BRANCH-NAME`
3. Each team member will push their changes up to github with `git push origin BRANCH-NAME`.
4. Each team member will open a **pull request** trying to merge their branch on github into `master`.  **Be very careful to make the PR against your forked repository and NOT AdaGold.**
    - To make the PR against your team members forked respository and not AdaGold, we will need to change the base repository
    - If there is a report of a merge conflict you will need to:
       - Pull the current state of a remote branch into **their feature branch** with `git pull origin <branch pulling FROM>`
       - in VS code select **accept both changes**
       - Resolve the merge conflicts by rearranging the recipe and commit the result
       - Push the result up to github with `git push origin BRANCH-NAME` or, if pushing from one branch to another, `git push <repo name> <from this branch>:<to this branch>`
       - Then attempt to merge their pull request.  If new changes have happened on master they may have to repeat step 1 above. 
5. Merge changes simultaneously, kind of like the _ad-hoc_ strategy.
    - **Remember**: Whoever on your team is merging their changes into master must successfully finish that process (including fixing any merge conflicts!) before the next person can begin.  Help them with resolving the conflicts.
    - Work with your fellow team members to resolve any merge conflicts.
6. Once everyone's changes have been merged together, the group as a whole should review it for completeness.
    - Make sure that none of the lines from your individual scrap are missing from the final result.
    - If there are any fixes needed, pick one person in the group to make the necessary changes and commit them.