# Wiping M1

Follow directions to start in macOS Recovery, wipe, and reinstall macOS

https://support.apple.com/guide/mac-help/macos-recovery-a-mac-apple-silicon-mchl82829c17/11.0/mac/11.0#mchl0e4c30d6

(Remember to erase both "Macintosh HD" and "Macintosh HD Data")

---

# Ada M1 Installfest

Chris's live demo:
https://adaacademy.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=3766a0f2-c498-4b51-a7d0-ac9e01835af7&start=undefined



- [ ] install Xcode's command line tools with: 

        $ xcode-select --install


- [ ] install homebrew, Git, and python3 with

        $ /bin/bash -c "$(curl -fsSL https://gist.githubusercontent.com/CheezItMan/2c883fc0c43ab44a5554d663995fe92e/raw/12cafa8e8d26c34d3d272c9da9c4402897dd4cca/install_python_apple_m1.bash)"


- [ ] Verify Homebrew installation (the following should prompt 'Your system is ready to brew')

        $ brew doctor 


- [ ] Verify Python, pip, git installation:
  
        $ python --version
        $ pip --version
        $ git --version


- [ ] Install VS Code: https://code.visualstudio.com


- [ ] In VS Code, type shift + cmd + p and type shell command to install the terminal shell command (one-time set up that allows you to open VS Code from the terminal)


- [ ] Install recommended VS Code extensions:
  
  - [ ] Live Share  - A way to collaborate on source code like Google Docs.
  - [ ] Markdown All in One  - An extension to help writing markdown files
  - [ ] Python  - The standard Python extension to provide syntax highlighting and code suggestions.
  - [ ] Indent Rainbow  - A nice extension to help you line up your indentations.
  - [ ] Bracket Pair Colorizer  - This extension colors matching brackets {} to match and make them easier to identify.
  - [ ] Python Test Explorer  - This extension lets you run tests individually in VS code via the Test Explorer UI.
  - [ ] ESLint  - A style checker for JavaScript code.


- [ ] From VS Code, open the command-palette with Shift-Command-P and enter Python: select interpreter


- [ ] Install Oh My Zsh

        $ sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"


- [ ] Install Rectangle

---

# Unit 2

- [ ] Install Postgres

- [ ] Install Postman

---