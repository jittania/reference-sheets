# Erase HD and Reinstall Big Sur

Follow directions to start in macOS Recovery, wipe, and reinstall macOS

https://support.apple.com/guide/mac-help/macos-recovery-a-mac-apple-silicon-mchl82829c17/11.0/mac/11.0#mchl0e4c30d6

(Remember to erase both "Macintosh HD" and "Macintosh HD Data")

---

# Ada Installfest



- [ ] Install Xcode's command line tools with: 

        $ xcode-select --install


- [ ] Install Homebrew, Pip 3, Python 3, Git (will need GitHub log in info), Node with:

        $ /bin/bash -c "$(curl -fsSL https://gist.githubusercontent.com/CheezItMan/e31aebdb0f686c1a194e980b24f3cea4/raw/5710e04d17a7840df3df0ea95502da275a9943cb/ada_c14_installfest.bash)"


- [ ] The Homebrew installation sequence offers some other optional things that you will also be prompted to install, and which are all recommended for Ada: Firefox, Google Chrome, VS Code, Slack

**Then make sure to quit and restart your terminal after Homebrew installation to ensure that this stuff works**


- [ ] Verify Homebrew installation (the following should prompt 'Your system is ready to brew')

        $ brew doctor 



- [ ] Verify Python, pip, git installation with:
  
        $ python --version
        $ pip --version
        $ git --version


- [ ] Verify that git was installed properly with:

        $ git config --get user.name
        $ git config --get user.email

Which should display your GitHub username and email address


- [ ] Install VS Code if you didn't during the Homebrew set up: https://code.visualstudio.com


- [ ] In VS Code, type shift + cmd + p and type shell command to install the terminal shell command (one-time set up that allows you to open VS Code from the terminal)


- [ ] Install recommended VS Code extensions:
  
  - [ ] Live Share  - A way to collaborate on source code like Google Docs.
  - [ ] Markdown All in One  - An extension to help writing markdown files
  - [ ] Python  - The standard Python extension to provide syntax highlighting and code suggestions.
  - [ ] Indent Rainbow  - A nice extension to help you line up your indentations.
  - [ ] Bracket Pair Colorizer  - This extension colors matching brackets {} to match and make them easier to identify.
  - [ ] Python Test Explorer  - This extension lets you run tests individually in VS code via the Test Explorer UI.
  - [ ] ESLint  - A style checker for JavaScript code.


- [ ] Set VS Code interpreter to Python: From VS Code, open the command-palette with Shift-Command-P and enter Python: select interpreter


- [ ] Optional: Set zsh as the default shell
  - [ ] Start termainl and go to "Preferences"
  - [ ] Then set the Shells open with: to /bin/zsh


- [ ] Optional: Install Oh My Zsh

        $ sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"


- [ ] Optional: Install Rectangle

---

# Unit 1

- [ ] Install pytest

        pip3 install -U pytest

---


# Unit 2

- [ ] Install Postgres

- [ ] Install Postman

---