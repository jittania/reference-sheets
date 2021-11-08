## **Git Commands: Quick Reference**
Syntax | Action
--- | ---
`git rebase master` | When run from a feature branch, moves the entire feature branch to begin on the tip of the main branch, effectively incorporating all of the new commits in main. But, instead of using a merge commit, rebasing re-writes the project history by creating brand new commits for each commit in the original branch.
`git merge master` | When run from a feature branch, will merge any changes made to local master branch into that feature branch
`git merge <feature-branch-name> master` | Creates a new “merge commit” in the feature branch that ties together the histories of both branches
`git stash` | Takes your uncommitted changes (both staged and unstaged), saves them away for later use, and then reverts them from your working copy
`git stash pop` | Popping your stash removes the changes from your stash and reapplies them to your working copy.
`git stash -u` | Tells git to also stash your untracked files i.e. new files in your working copy that have not yet been staged and/or files that have been ignored 
`git branch <name for duplicated branch>` | Makes a duplicate branch of the one you're currently on 
`git status` | Displays the status of your working directory. Options include new, staged, and modified files. It will retrieve branch name, current commit identifier, and changes pending commit.
`git diff <file>` | Show changes between working directory and staging area
`git diff --staged <file>` | Shows any changes between the staging area and the repository.
`git branch` | lists existing branches 
`git diff HEAD` | after a `git add` command, this command will list show the changes made since most recent commit
`git switch <destination-branch-name>` | switch to an existing branch (new)
`git checkout <existing_branch>` | switch to an existing branch (old-school)
`git branch <new-branch-name>` | create a new branch
`git checkout -b <new_branch>` | create a new branch and switch to it
`git branch -m <new_name>` | rename a LOCAL branch. must be on the branch that you want to rename 
`git branch -d localBranchName` | delete branch locally
`git push origin --delete remoteBranchName` | delete branch remotely
`git remote` | Shows names of remote repositories 
`git remote -v` | Shows names and URLs of remote repositories 
`git config --global push.default current` | One-time optional commnand!! This will ensure that when you run only git push without specifying the branch name, it will push to the remote repo from the local machine’s existing branch to the same branch in remote repo. That is, it should push the current branch to update a branch with the same name on the receiving end.
`git push <repo name> <branch name>` | general syntax for pushing to specific repo and branch
`git push <repo name> <from this branch>:<to this branch>` | optional syntax for pushing from one branch to another
`git reset --soft HEAD~1` | The easiest way to undo the last Git commit is to execute the “git reset” command with the “–soft” option that will preserve changes done to your files. You have to specify the commit to undo which is `HEAD~1` in this case (`HEAD~1` means that you want to reset the HEAD (the last commit) to one commit before in the log history)

---

## **Git Set Up**

### **If you already have a remote repo set up on GitHub:**

1.  Create a local folder for project 
2.  `git clone`  followed by the link to your GitHub project repo

### **If you've already created a project repo locally and want to put a remote repo on GitHub:**

1.  Projects are not tracked with Git (and therefore don't use Git) until it is initialized as a Git project. To turn any folder into a Git project, run this command in the project root: `git init`
2.  Create an empty repo on GitHub
3.  Link the local repository to an empty GitHub repository using the following command: `git remote add origin [url]`

---

## **Git Workflow**

1. Run `git checkout master` to make sure you're on master branch
2. Fetch and merge any new commits from master branch with `git pull`
3. Create a new branch with `git checkout -b <new branch name>`
4. When you have a small, meaningful change, get ready to make a commit:
   1. Confirm that the project is in the state you expect with `git status`
   2. Move the intended changes from local changes area to staging with one of the following:
         - `git add name_of_file` (adding specific file(s))
         - `git add .` (to select all files under the current directory)
         - `git add -p` 
            - This starts an interactive mode where local code changes will be presented on the screen one at a time.
            - At each chunk, we can decide whether the change should go into staging: `y` then enter for "yes," `n` then enter for "no."
            - This mode cycles through all chunks in the local changes area, then exits the interactive mode
            - This method encourages reviewing code changes
    3. Create a commit and a commit message from the changes in staging with `git commit -m ""`
    4. Review the commit with `git show`, then exit that view and get back to command line with `q`
5. Go back to the master branch and fetch and merge any new commits with `git pull`
    - Note: If pulling FROM from a particular remote branch other than `master`, use `git pull origin <branch pulling FROM>`
    - If there are changes, will need to switch back to your feature branch and from there run `git merge master` to pull those changes in from `master` to the branch you are currently on 
6.  Send all of your commits to `origin` with `git push`, or for more specificity, use `git push origin BRANCH-NAME` 
    -  Note: If pushing from one branch to another (usually `main`), `git push <repo name> <from this branch>:<to this branch>`
7.  Review your work with `git status` and `git log`

---

## **Resolving Merge Conflicts**

Conflicts generally arise when two people have changed the same lines in a file, or if one developer deleted a file while another developer was modifying it. In these cases, Git cannot automatically determine what is correct. Conflicts only affect the developer conducting the merge, the rest of the team is unaware of the conflict.

A merge can enter a conflicted state at two separate points:

1. **Git fails to start the merge**

A merge will fail to start when Git sees there are changes in either the working directory or staging area of the current project. Git fails to start the merge because these pending changes could be written over by the commits that are being merged in. When this happens, it is not because of conflicts with other developer's, but conflicts with pending local changes. The local state will need to be stabilized using `git stash`, `git checkout`, `git commit` or `git reset`. This is what the error will look like: 

    error: Entry '<fileName>' not uptodate. Cannot merge. (Changes in working directory)


2. **Git fails during the merge**

A failure DURING a merge indicates a conflict between the current local branch and the branch being merged. This indicates a conflict with another developers code, and you'll get an error like this:

    error: Entry '<fileName>' would be overwritten by merge. Cannot merge. (Changes in staging area)


### **More Merge Troubleshooting**

```
"Updates were rejected because the tip of your current branch is behind its remote counterpart. Integrate the remote changes (e.g. hint: ‘git pull …’) before pushing again
```

This happens because, after you've pulled, someone pushed changes to the same branch you're working on.

Tentative steps for how to solve (based on my experience - will probably update this in the future):
1.  After receiving the above error, run `git pull origin <feature branch causing conflicts>` which will attempt to pull down changes from the remote version of this branch. This will set off a merge conflict warning and fail.
2.  Once the merge conflicts have been triggered, you can go into VS Code and review them. You have to go through each conflict and decide whether to accept the current changes vs. the incoming changes, or attempt to reconcile both. You'll know you're done resolving all of the conflicts once VS Code removes the red error flags on the files causing the conflicts.
3. Now re-add the files (I find using `git add -p` particularly useful here to help make sense of what's happening) and commit the changes
4. Now attempt to push again with `git push origin <feature branch>`

```
Please enter a commit message to explain why this merge is necessary,
especially if it merges an updated upstream into a topic branch.
```
How to respond to this vim window (and get out of it):

1. press "i" (i for insert)
2. write your merge message
3. press "esc" (escape)
4. write ":wq" (write & quit)
5. then press enter
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



